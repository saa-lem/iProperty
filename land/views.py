from __future__ import unicode_literals

from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView,RedirectView,CreateView
from rest_framework.generics import GenericAPIView,RetrieveAPIView ,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework import  mixins,generics
from django.http import HttpResponse
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PropertySerializer,PropertyCreateSerializer,PropertyDeleteSerializer,PropertyUpdateSerializer
from .models import Property
from .forms import  UserUpdateForm, PostPropertyForm
from itertools import chain
# Create your views here.
class PropertyView(APIView):
    def get(self, request):
        properties = Property.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = PropertySerializer(properties, many=True)
        return Response({"properties": serializer.data})
   
class PropertyCreateAPIView(CreateAPIView):
  queryset = Property.objects.all()
  serializer_class = PropertyCreateSerializer
    
class PropertyUpdateAPIView(UpdateAPIView):
  queryset = Property.objects.all()
  serializer_class = PropertyUpdateSerializer

class PropertytDestroyAPIView(DestroyAPIView):
  queryset = Property.objects.all()
  serializer_class = PropertyDeleteSerializer
class UserPropertyListView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','location']
  









