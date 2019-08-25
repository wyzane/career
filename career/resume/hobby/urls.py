from django.urls import path

from .apis.views import (HobbyList,
                         HobbyDetail,
                         Test)
from .apis.views_crud import (HobbyCreation,
                              HobbyDeletion,
                              HobbyUpdate)


urlpatterns = [
    path('list/hobby',
         HobbyList.as_view()),
    path('detail/hobby',
         HobbyDetail.as_view()),
    path('create/hobby',
         HobbyCreation.as_view()),
    path('delete/hobby',
         HobbyDeletion.as_view()),
    path('update/hobby',
         HobbyUpdate.as_view()),
    path("test/hobby",
         Test.as_view())
]
