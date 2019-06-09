from django.urls import path

from .views import IndexList


urlpatterns = [
    path('list/index',
         IndexList.as_view()),
]
