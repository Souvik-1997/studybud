from django.urls import path
from base.views import AuthView


urlpatterns = [
    #login urls
    path("login/", AuthView.authLogin, name="login"),
    path("logout/", AuthView.authLogout, name="logout"),
    path("signup/", AuthView.authSignup, name="signup"),
    path("profile/<str:pk>/", AuthView.userProfile, name="profile"),

]