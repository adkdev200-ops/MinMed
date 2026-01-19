"""
URL configuration for MinMed project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
import users.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users.views.home_page, name = 'home'),
    path('base', users.views.base_page),
    path('login', users.views.login_page,  name='login'),
    path('signup', users.views.signup_page, name = 'signup'),
    path('logout', users.views.logout_view, name ='logout'),
    path('upload', users.views.upload_page, name ='upload'),
    path('like-post/', users.views.like_post, name ='like-post'),
    path('profile/<username>', users.views.profile, name = 'profile'),
    path('add-comment/', users.views.add_comment, name ='add-comment'),
    path('update-info', users.views.update_info, name = 'update-info')

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )