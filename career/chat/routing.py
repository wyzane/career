from django.urls import path

from . import consumers

urlpatterns = [
    path('ws/chat/<service_name>', consumers.ChatConsumer),
    path('ws/chat01/<service_name>', consumers.ChatConsumer01),
    path('ws/chat02/<service_name>', consumers.ChatConsumer02),
]
