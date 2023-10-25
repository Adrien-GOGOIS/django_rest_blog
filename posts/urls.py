from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, 'post')
router.register(r'users', UserViewSet, 'user')

urlpatterns = [
    path('', include(router.urls)),
]