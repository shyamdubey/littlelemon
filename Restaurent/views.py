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



class MenuViewSet(viewsets.ModelViewSet):
    permission_classes = IsAuthenticated
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = IsAuthenticated
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class MenuItemView(generics.ListCreateAPIView):
    permission_classes = IsAuthenticated
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = IsAuthenticated
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

