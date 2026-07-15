from django.shortcuts import render
from rest_framework import viewsets
from .models import Cars
from .serializer import CarsSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

class CarsList(ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    
class CarCreate(CreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

class CarUpdate(RetrieveUpdateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

class CarDelete(RetrieveUpdateDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    
class CarUpdateDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    

    