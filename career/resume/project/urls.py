from django.urls import path

from .apis.views import (ProjectList, ProjectDetail)
from .apis.views_crud import (ProjectCreation,
                              ProjectDeletion,
                              ProjectUpdate)


urlpatterns = [
    path('create/project',
         ProjectCreation.as_view()),
    path('list/project',
         ProjectList.as_view()),
    path('detail/project',
         ProjectDetail.as_view()),
    path('delete/project',
         ProjectDeletion.as_view()),
    path('update/project',
         ProjectUpdate.as_view()),
]