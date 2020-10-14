from django.conf.urls import url
from django.conf import settings
from django.urls import re_path

from . import views
from smartpages.views import SmartPageView


app_name = 'spacescoops'

urlpatterns = [
    url(r'^$', views.ArticleListView.as_view(), name='list'),
    url(r'^feed/$', views.ArticleFeed(), name='feed'),
    url(r'^(?P<code>\d{4})/$', views.detail_by_code),
    # url(r'^(?P<code>\d{4})/pdf/$', views.ArticlePDFView.as_view(), name='pdf'),
    url(r'^(?P<code>\d{4})/(?P<slug>.+)?/$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^institution/(?P<institution>.+)/$', views.ArticleListView.as_view(), name='list_by_institution'),
    re_path(r'^(?P<url>.*/)$', SmartPageView.as_view(), name='smartpage'),
]
