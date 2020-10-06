from django.db.models.query import Prefetch
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render
from parler.views import TranslatableSlugMixin, ViewUrlMixin
from django.contrib.syndication.views import Feed
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.utils.translation import get_language
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from .models import Article, Category, ArticleTranslation
from django_ext import compiler
from institutions.models import Institution

def home(request):
    try:
        articles = Article.objects.featured().active_translations()
        featured = Article.add_prefetch_related(articles)[:4]
    except:
        articles = Article.objects.none()
        featured = []

    try:
        categories = Category.objects.all()
    except:
        categories = Category.objects.none()
    return render(request, 'home.html', {
        'featured': featured,
        'categories': categories,
    })

def search(request):
    pass

def _article_queryset(request, only_translations=True):
    qs = Article.objects.available(user=request.user)
    if only_translations:
        qs = qs.active_translations()
    # qs = qs.prefetch_related('translations')
    # qs = qs.prefetch_related('categories')
    # qs = qs.prefetch_related('images__file')
    qs = Article.add_prefetch_related(qs)
    return qs


class ArticleListView(ViewUrlMixin, ListView):
    # template_name = 'articles/article_list.html'
    page_template_name = 'spacescoops/article_list_page.html'
    # context_object_name = 'object_list'
    # model = Article
    view_url_name = 'scoops:list'
    # paginate_by = 10

    def get_queryset(self):
        qs = _article_queryset(self.request)
        if 'category' in self.kwargs:
            category = self.kwargs['category']
            qs = qs.filter(**{category: True})
        if 'institution' in self.kwargs:
            institution = self.kwargs['institution']
            qs = qs.filter(originalnews__institution__slug=institution)
        return qs

    def get_view_url(self):
        if 'category' in self.kwargs:
            return reverse('scoops:list_by_category', kwargs={'category': self.kwargs['category']})
        if 'institution' in self.kwargs:
            return reverse('scoops:list_by_institution', kwargs={'institution': self.kwargs['institution']})
        else:
            return super().get_view_url()

    def get_template_names(self):
        if self.request.is_ajax():
            return [self.page_template_name]
        else:
            return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_template'] = self.page_template_name
        context['category'] = self.kwargs.get('category', '')
        return context


class ArticleDetailView(DetailView):
    # model = Article
    # template_name = 'spacescoops/article_detail.html'
    slug_field = 'code'
    slug_url_kwarg = 'code'

    def get_queryset(self, only_translations=False):
        qs = _article_queryset(self.request, only_translations=only_translations)
        qs = qs.prefetch_related('originalnews_set')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random'] = self.get_queryset(only_translations=True).order_by('?')[:3]
        return context

    def get(self, request, *args, **kwargs):
        fmt = request.GET.get('format')
        if hasattr(settings, 'SPACESCOOP_DOWNLOADS') and fmt in settings.SPACESCOOP_DOWNLOADS['renderers'].keys():
            code = kwargs[self.slug_url_kwarg]
            url = compiler.get_generated_url(settings.SPACESCOOP_DOWNLOADS, fmt, code, lang=get_language())
            if not url:
                raise Http404
            return redirect(url)
        else:
            return super().get(request, args, kwargs)


class ArticleDetailPrintView(ArticleDetailView):
    template_name = 'spacescoops/article_detail_print.html'

class ArticlePDFView(DetailView):
    """Generate a pdf from the detailview, and append and file attachments to the end
    """
    model = Article
    slug_field = 'code'
    slug_url_kwarg = 'code'

    def render_to_response(self, context, **kwargs):
        context['pdf'] = True
        pdf_response = HttpResponse(content_type='application/pdf')
        response = super().render_to_response(context, **kwargs)
        response.render()
        try:
            pdf = self.object.translations.get(language_code=get_language()).generate_pdf()
        except ObjectDoesNotExist:
            pdf = self.object.translations.get(language_code='en').generate_pdf(no_trans=True)
        except Exception as exc:
            error = 'There was an error generating your pdf. {}'
            messages.error(self.request, error.format(str(exc)))
            return HttpResponseRedirect(reverse('home'))
        pdf_response.write(pdf)
        filename = f"scoop-{self.object.code}-{get_language()}.pdf"
        pdf_response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return pdf_response


def detail_by_code(request, code):
    'When only the code is provided, redirect to the canonical URL'
    try:
        obj = _article_queryset(request).get(code=code)
    except Article.DoesNotExist:
        raise Http404(_('Article does not exist'))
    return redirect(obj, permanent=True)


class ArticleFeed(Feed):
    title = 'Space Scoop'
    link = '/'
    # link = reverse('scoops:list')
    # description = ''

    def items(self):
        return Article.objects.available().translated()[:9]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.story

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('scoops:detail', kwargs={'code': item.code, 'slug': item.slug})


def _category_queryset(request):
    qs = Category.objects.all()
    # qs = qs.active_translations()  # this will disable categories for "untranslated" languages
    qs = qs.prefetch_related('articles__categories__translations')
    qs = qs.prefetch_related('translations')
    # return Category.add_prefetch_related(qs)
    return qs


class CategoryListView(ViewUrlMixin, ListView):
    # template_name = 'categories/category_list.html'
    # context_object_name = 'object_list'
    # model = Category
    view_url_name = 'categories:list'

    def get_queryset(self):
        qs = _category_queryset(self.request)
        return qs


class CategoryDetailView(TranslatableSlugMixin, DetailView):
    # model = Category
    # template_name = 'categories/category_detail.html'

    def get_language_choices(self):
        return [self.get_language(), 'en']  # TODO: nasty hack!

    def get_queryset(self):
        qs = _category_queryset(self.request)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = context['object'].articles.active_translations()
        return context


def _partner_queryset(request):
    scoops_prefetch = Prefetch('scoops', queryset=Article.objects.available(user=request.user).filter(images__isnull=False).distinct(), to_attr='scoops_available')
    qs = Institution.objects.all().prefetch_related(scoops_prefetch)

    return qs


class PartnerListView(ListView):
    template_name = 'spacescoops/partner_list.html'
    view_url_name = 'partners:list'

    def get_queryset(self):
        qs = _partner_queryset(self.request).order_by('-spacescoop_count')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class PartnerDetailView(DetailView):
    template_name = 'spacescoops/partner_detail.html'

    def get_queryset(self):
        qs = _partner_queryset(self.request)
        return qs
