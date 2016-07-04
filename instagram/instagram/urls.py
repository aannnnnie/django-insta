"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from content.views import UserView, CreatePostView, home_view, PostView, profile_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^accounts/profile/$', profile_view),
    url(r'^$', home_view, name='home'),
    url(r'^upload/$', CreatePostView.as_view(), name='create-post'),
    url(r'^user/(?P<pk>[0-9]+)', UserView.as_view(), name='user'),
    url(r'^media/(?P<pk>[0-9]+)', PostView.as_view(), name='post'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
