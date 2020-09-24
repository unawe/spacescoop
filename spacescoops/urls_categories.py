from django.conf.urls import url

from . import views

app_name = 'spacescoops'

urlpatterns = [
    url(r'^$', views.CategoryListView.as_view(), name='list'),
    url(r'^(?P<slug>.+)?/$', views.CategoryDetailView.as_view(), name='detail'),
]
