"""icas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import User

from snippets.views import SnippetViewSet, UserViewSet
#from images.views import ImageViewSet, S3ViewSet

from rest_framework.routers import DefaultRouter


# Retrive the URL for the /icas/{media, static} directories
staticurl = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
mediaurl = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
#router.register(r'images', ImageViewSet, base_name='images')
#router.register(r's3', S3ViewSet, base_name='s3')
#router.register(r'snippets', SnippetViewSet, base_name='snippet')
router.register(r'users', UserViewSet, base_name='user')

urlpatterns = [
    url(r'^api/wadl/', include(router.urls)),
    url(r'^admin/', admin.site.urls, name='admin'),
]

# Add /icas/{media, static} directories URL
urlpatterns += (staticurl + mediaurl)

# Wire up our API using automatic URL routing.
# Additionally, we Django-REST includes login URLs for the browsable API.
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
