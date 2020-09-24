from django.test import TestCase

from datetime import timedelta
from django.utils.timezone import now
from django.core.urlresolvers import reverse

from .models import Article


class ArticlesTestCase(TestCase):

    create_article_running_code = 9900

    # def login_user(self, user):
    #     return self.client.login(username=user.username, password=user.password)

    def create_user(self, username, groups=[], password=None):
        from django.contrib.auth.models import User, Group
        u = User.objects.create(username=username)
        u.set_password(password)
        for groupname in groups:
            g, created = Group.objects.get_or_create(name=groupname)
            if created:
                g.save()
            u.groups.add(g)
        u.save()
        return u

    def create_article(self, name, release_date=now(), embargo_date=None, published=False, featured=False):
        self.create_article_running_code += 1
        return Article.objects.create(
                code='%04d'%self.create_article_running_code,
                slug=name, title=name,
                release_date=release_date,
                embargo_date=embargo_date,
                published=published,
                featured=featured)

    def setUp(self):

        self.user = self.create_user(username='testuser', password='p', groups=['staff'])
        self.press_user = self.create_user(username='pressuser', password='p', groups=['press'])

        one_minute = timedelta(minutes=1)

        # print(Article.__mro__)
        self.obj_draft = self.create_article('draft', release_date=now()+one_minute, published=False)
        self.obj_ready = self.create_article('ready', release_date=now()+one_minute, published=True)
        self.obj_embargoed = self.create_article('embargoed', release_date=now()+one_minute, published=True, embargo_date=now()-one_minute)
        self.obj_released = self.create_article('released', release_date=now()-one_minute, published=True)
        self.obj_featured = self.create_article('featured', release_date=now()-one_minute, published=True, featured=True)
        self.obj_retracted = self.create_article('retracted', release_date=now()-one_minute, published=False)


class PublishingTests(ArticlesTestCase):
    longMessage = True

    def test_is_released(self):
        self.assertFalse(self.obj_draft.is_released())
        self.assertFalse(self.obj_ready.is_released())
        self.assertFalse(self.obj_embargoed.is_released())
        self.assertTrue(self.obj_released.is_released())
        self.assertTrue(self.obj_featured.is_released())
        self.assertFalse(self.obj_retracted.is_released())

    def test_is_embargoed(self):
        self.assertFalse(self.obj_draft.is_embargoed())
        self.assertTrue(self.obj_ready.is_embargoed())  # Note: no embargo date, means visible to embargo
        self.assertTrue(self.obj_embargoed.is_embargoed())
        self.assertFalse(self.obj_released.is_embargoed())
        self.assertFalse(self.obj_featured.is_embargoed())
        self.assertFalse(self.obj_retracted.is_embargoed())

    def test_manager_release(self):
        objects = Article.objects.available()
        self.assertNotEqual(len(objects), 0)
        self.assertEqual(len(objects), 2)
        for obj in objects:
            self.assertTrue(obj.is_released())

    def _test_manager_user_available(self):
        objects = Article.objects.available(user=self.user)
        self.assertEqual(len(objects), 6)

    def _test_manager_user_embargo(self):
        objects = Article.objects.available(user=self.press_user)
        self.assertEqual(len(objects), 4)
        for obj in objects:
            self.assertTrue(obj.is_released() or obj.is_embargoed())

    def test_manager_user_available_login_required(self):
        from django_ext.models import publishing_login_required
        Article.PublishingMeta.permission_all = publishing_login_required()
        self._test_manager_user_available()

    def test_manager_user_embargo_login_required(self):
        from django_ext.models import publishing_login_required
        Article.PublishingMeta.permission_all = None
        Article.PublishingMeta.permission_embargoed = publishing_login_required()
        self._test_manager_user_embargo()

    def test_manager_user_available_group_required(self):
        from django_ext.models import publishing_group_required
        Article.PublishingMeta.permission_all = publishing_group_required('staff')
        self._test_manager_user_available()

    def test_manager_user_embargo_group_required(self):
        from django_ext.models import publishing_group_required
        Article.PublishingMeta.permission_all = publishing_group_required('staff')
        Article.PublishingMeta.permission_embargoed = publishing_group_required('press')
        self._test_manager_user_embargo()

    def test_manager_user_available_permission_required(self):
        pass  # TODO

    def test_manager_user_embargo_permission_required(self):
        pass  # TODO

    def test_manager_user_available_user_passes_test(self):
        pass  # TODO

    def test_manager_user_embargo_user_passes_test(self):
        pass  # TODO

    def test_manager_embargoed(self):
        objects = Article.objects.embargoed()
        self.assertNotEqual(len(objects), 0)
        for obj in objects:
            self.assertTrue(obj.is_embargoed())

    def test_featured(self):
        objects = Article.objects.featured()
        self.assertNotEqual(len(objects), 0)
        for obj in objects:
            self.assertTrue(obj.featured)

    def test_not_released_reason(self):
        objects = Article.objects.all()
        for obj in objects:
            self.assertEqual(not obj.is_released(), bool(obj.not_released_reason()), msg=str(obj.not_released_reason()))


class ArticlesEmptyListViewTests(TestCase):
    def test_empty(self):
        '''
        If no items exist, an appropriate message should be displayed.
        '''
        response = self.client.get(reverse('scoops:list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], [])
        self.assertContains(response, 'No articles are available.')


class ArticlesListViewTests(ArticlesTestCase):
    pass


class ArticlesDetailViewTests(ArticlesTestCase):
    longMessage = True

    # def setUp(self):
    #     super().setUp()
    #     from django_ext.models import publishing_group_required
    #     Article.PublishingMeta.permission_all = publishing_group_required('staff')
    #     Article.PublishingMeta.permission_embargoed = publishing_group_required('press')

    # All logged user can access all articles, hence there are no need for "embardo users"

    def test_draft(self):
        response = self.client.get(self.obj_draft.get_absolute_url())
        self.assertEqual(response.status_code, 404)

        # self.client.login(username='pressuser', password='p')
        # response = self.client.get(self.obj_draft.get_absolute_url())
        # self.assertEqual(response.status_code, 404)

        self.client.login(username='testuser', password='p')
        response = self.client.get(self.obj_draft.get_absolute_url())
        self.assertContains(response, self.obj_draft.title, status_code=200)

    def test_embargoed(self):
        response = self.client.get(self.obj_embargoed.get_absolute_url())
        self.assertEqual(response.status_code, 404)

        # self.client.login(username='pressuser', password='p')
        # response = self.client.get(self.obj_embargoed.get_absolute_url())
        # self.assertContains(response, self.obj_embargoed.title, status_code=200)

        self.client.login(username='testuser', password='p')
        response = self.client.get(self.obj_embargoed.get_absolute_url())
        self.assertContains(response, self.obj_embargoed.title, status_code=200)

    def test_released(self):
        response = self.client.get(self.obj_released.get_absolute_url())
        self.assertContains(response, self.obj_released.title, status_code=200)

        # self.client.login(username='pressuser', password='p')
        # response = self.client.get(self.obj_released.get_absolute_url())
        # self.assertContains(response, self.obj_released.title, status_code=200)

        self.client.login(username='testuser', password='p')
        response = self.client.get(self.obj_released.get_absolute_url())
        self.assertContains(response, self.obj_released.title, status_code=200)
