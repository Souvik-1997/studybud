from django.urls import include, path
from base.views import HomeView


urlpatterns = [
    path("", HomeView.home, name="home"),
    
    # User authentication urls
    path("auth/", include("base.urls.auth")), #Group Url
    
    # Room urls
    path("room/", include("base.urls.room")) #Group Url
]
