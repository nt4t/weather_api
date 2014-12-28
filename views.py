from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from weather.models import Weather
from weather.serializers import WeatherSerializer
from weather.serializers import UserSerializer

from rest_framework import generics

from django.contrib.auth.models import User

from rest_framework import permissions
from weather.permissions import IsOwnerOrReadOnly

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WeatherList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class WeatherDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
#    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
