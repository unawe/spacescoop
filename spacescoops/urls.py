from django.conf.urls import url
from django.conf import settings

from . import views

app_name = 'spacescoops'

urlpatterns = [
    url(r'^$', views.ArticleListView.as_view(), name='list'),
    url(r'^feed/$', views.ArticleFeed(), name='feed'),
    url(r'^(?P<code>\d{4})/$', views.detail_by_code),
    url(r'^(?P<code>\d{4})/print-preview/$', views.ArticleDetailPrintView.as_view(), name='print-preview'),
    # url(r'^(?P<code>\d{4})/print/$', views.article_pdf, name='print'),
    url(r'^(?P<code>\d{4})/(?P<slug>.+)?/$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^institution/(?P<institution>.+)/$', views.ArticleListView.as_view(), name='list_by_institution')
    ]
