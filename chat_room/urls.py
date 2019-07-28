from django.urls import path
from chat_room.views import *

urlpatterns = [
    path('room', RoomView.as_view(), name='rooms_list'),
]
