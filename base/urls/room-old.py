from django.urls import path
from .views import HomeView
from .views.HomeView import RoomView 


# urlpatterns = [
#     path("<str:pk>/", views.room, name="room"),
#     path("create", views.createRoom, name="create-room"),
#     path("update/<str:pk>", views.updateRoom, name="update-room"),

#     path("topics", views.topics, name="topics"),
# ]

urlpatterns = [
    path("<str:pk>/", RoomView.as_view()),
]
