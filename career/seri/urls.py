from django.urls import path

from .views import StudentList, StudentCreation


urlpatterns = [
    path('detail/student',
         StudentList.as_view()),
    path('creation/student',
         StudentCreation.as_view()),
]
