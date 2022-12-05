from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import MaterialsSerializer
from .models import Materials, Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import *
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from users import authentication
from .permissions import *
# Create your views here.


class MaterialsAPIListPaginamtion(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
class MaterialsAPIList(generics.ListCreateAPIView):
    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializer
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (IsTeacher,)
    pagination_class = MaterialsAPIListPaginamtion

class MaterialsAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializer
    #permission_classes = (permissions.IsAuthenticated, )

class MaterialsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializer
    #permission_classes = (permissions.IsAuthenticated, )
