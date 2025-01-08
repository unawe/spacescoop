"""spacescoop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.static import serve

from smartpages.views import SmartPageView
from spacescoops.views import home
from search.views import simplesearch


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('taggit_autosuggest/', include('taggit_autosuggest.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]

urlpatterns += i18n_patterns(
    path('', home, name='home'),
    path('scoops/', include('spacescoops.urls', namespace='scoops')),
    path('topics/', include('spacescoops.urls_categories', namespace='categories')),
    path('friends/', include('spacescoops.urls_partners', namespace='partners')),
    path('words/', include('glossary.urls', namespace='glossary')),
    path('search/', simplesearch, name='search'),
    path('<url>/', SmartPageView.as_view(), name='smartpage'),
)
