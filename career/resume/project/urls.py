from django.urls import path

from .apis.views import (ProjectList)
from .apis.views_crud import (ProjectCreation)


urlpatterns = [
    path('create/project',
         ProjectCreation.as_view()),
    path('list/project',
         ProjectList.as_view()),
]