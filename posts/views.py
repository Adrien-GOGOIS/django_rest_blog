from django.shortcuts import render
from rest_framework import viewsets

from .models import Post, User
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all().order_by('-date_joined')