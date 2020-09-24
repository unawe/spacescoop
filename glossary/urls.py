from django.conf.urls import url

from . import views

app_name = 'glossary'

urlpatterns = [
    url(r'^$', views.EntryListView.as_view(), name='list'),
    url(r'^(?P<slug>.+)?/$', views.EntryDetailView.as_view(), name='detail'),
]
