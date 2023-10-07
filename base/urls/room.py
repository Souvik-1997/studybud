from django.urls import path
from base.views import RoomView


urlpatterns = [
    #Room urls
    path("<str:pk>/", RoomView.room, name="room"),
    path("create", RoomView.createRoom, name="create-room"),
    path("update/<str:pk>", RoomView.updateRoom, name="update-room"),
    path("delete/<str:pk>", RoomView.deleteRoom, name="delete-room"),
    path("delete/message/<str:pk>", RoomView.deleteMessage, name="delete-message"),

    #Topic urls
    path("topics", RoomView.topics, name="topics")
]
