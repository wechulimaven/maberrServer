from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from . import models
from .serializer import PostSerializer


class ListPost(generics.ListCreateAPIView):
    queryset = models.Posts.objects.all()
    serializer_class = PostSerializer


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Posts.objects.all()
    serializer_class = PostSerializer
