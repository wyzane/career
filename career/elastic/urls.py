from django.urls import path

from .views import (IndexList,
                    IndexCreation,
                    IndexRebuild)


urlpatterns = [
    path('list/index',
         IndexList.as_view()),
    path('create/index',
         IndexCreation.as_view()),
    path('rebuild/index',
         IndexRebuild.as_view()),
]
