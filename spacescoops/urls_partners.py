from django.conf.urls import url

from . import views

app_name = 'spacescoops'

urlpatterns = [
    url(r'^$', views.PartnerListView.as_view(), name='list'),
    url(r'^(?P<slug>.+)?/$', views.PartnerDetailView.as_view(), name='detail'),
]
