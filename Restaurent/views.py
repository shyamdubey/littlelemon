from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from .serializers import *

# Create your views here.


def sayHello(request):
    return HttpResponse("hello world!")


def index(request):
    return render(request, 'index.html', {})


