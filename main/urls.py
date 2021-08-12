from django.contrib import admin
from django.urls import path
from .views import index, TweetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api', TweetViewSet, basename='tweet')

urlpatterns = [
    path('', index)
]
urlpatterns += router.urls
