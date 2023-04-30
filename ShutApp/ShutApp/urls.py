'''ShutApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
'''

from ShutApp import settings
from django.conf.urls.static import static
from django.contrib.auth.views import auth_logout
from django.contrib import admin
from django.urls import path, include
from Main.views import *
from Login.views import *
from Registration.views import *
from Privacy.views import *
from PasswordReset.views import *
from Messenger.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', main_page, name='main'),
    path('login/', login_page, name='login'),
    path('register/', registration_page, name='register'),
    path('privacy/', privacy_page, name='privacy'),
    path('password_reset/', password_reset_page, name='password_reset'),
    path('messenger/', messenger_page, name='messenger'),
    path('messenger/<str:username>', user_page, name='user'),
    path('messenger/dm/<str:username>', dm_page, name='dm'),
    path('messenger/people/', people_page, name='people'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
