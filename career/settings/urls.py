"""career URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

import resume.skill.urls as url_skill
import resume.project.urls as url_project
import resume.hobby.urls as url_hobby
import account.user.urls as url_user
import elastic.urls as url_elastic
import chat.urls as url_chat
import seri.urls as url_seri

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/resume/', include(url_skill)),
    path('api/v1/resume/', include(url_project)),
    path('api/v1/resume/', include(url_hobby)),
    path('api/v1/account/', include(url_user)),
    path('api/v1/elastic/', include(url_elastic)),
    path('api/v1/user/', include(url_chat)),
    path('api/v1/seri/', include(url_seri)),
]
