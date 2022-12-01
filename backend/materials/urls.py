from django.contrib import admin
from django.urls import path, include, re_path
from materials.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
urlpatterns = [
    path('materials/', MaterialsAPIList.as_view()),
    path('materials/<int:pk>/', MaterialsAPIUpdate.as_view()),
    path('materials/delete/<int:pk>/', MaterialsAPIDestroy.as_view()),
]
