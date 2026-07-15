from django.shortcuts import render
from rest_framework import viewsets
from .models import Cars
from .serializer import CarsSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

class BookList(ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    
class BookCreate(CreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

class BokkUpdate(RetrieveUpdateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

class BookDelete(RetrieveUpdateDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    
class BookUpdateDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    

    