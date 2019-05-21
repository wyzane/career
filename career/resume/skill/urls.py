# @Author : WZ 
# @Time : 2019/5/17 21:42 
# @Intro :

from django.urls import path

from .apis.views import (SkillList, SkillDetail)
from .apis.views_crud import (SkillCreation,
                              SkillUpdate,
                              SkillDeletion)


urlpatterns = [
    path('create/skill',
         SkillCreation.as_view()),
    path('list/skill',
         SkillList.as_view()),
    path('detail/skill',
         SkillDetail.as_view()),
    path('update/skill',
         SkillUpdate.as_view()),
    path('delete/skill',
         SkillDeletion.as_view()),
]
