from django.shortcuts import render
from .models import Tweet
from rest_framework import viewsets
from .serializer import TweetSerializer
# Create your views here.


class TweetViewSet(viewsets.ModelViewSet):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()


# class
def index(request):
    return render(request, template_name='main/index.html')
