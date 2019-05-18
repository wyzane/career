# @Author : WZ 
# @Time : 2019/5/17 21:42 
# @Intro :

from django.urls import path

from .apis.views_crud import (SkillCreation)


urlpatterns = [
    path('create/skill',
         SkillCreation.as_view()),
]
