from django.urls import path
from . import apis
from . import views
urlpatterns = [
    path('register/', apis.RegisterApi.as_view(), name="register"),
    path('login/', apis.LoginApi.as_view(), name="login"),
    path('profile/user/',apis.UserApi.as_view(), name="me"),
    path('logout/', apis.LogoutApi.as_view(), name="logout"),
]
