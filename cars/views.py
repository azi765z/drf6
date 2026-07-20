from django.shortcuts import render
from rest_framework import viewsets
from .models import Cars
from .serializer import CarsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

# class CarsList(ListAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = CarsSerializer
    
# class CarCreate(CreateAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = CarsSerializer

# class CarUpdate(RetrieveUpdateAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = CarsSerializer

# class CarDelete(RetrieveUpdateDestroyAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = CarsSerializer
    
# class CarUpdateDestroyAPIView(RetrieveDestroyAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = CarsSerializer

@api_view(['GET'])
def cars_listview(request):
    cars = Cars.objects.all()
    serializer = CarsSerializer(cars,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def cars_create(request):
    serializer = CarsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({"message": "Cars Create Error"})

@api_view(['GET'])
def car_detail(request,pk):
    car = Cars.objects.get(pk=pk)
    serializer = CarsSerializer(car)
    return Response(serializer.data)

@api_view(['PUT'])
def car_update(request,pk):
    car = Cars.objects.get(pk=pk)
    serializer = CarsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({'errors'})



@api_view(['DELETE'])
def cars_delete(request,pk):
    car = Cars.objects.get(pk=pk)
    car.delete()
    return Response({'message': 'User deleted'})

@api_view(['PATCH'])
def cars_patch(request,pk):
    car = Cars.objects.get(pk=pk)
    serializer = CarsSerializer(car, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({'errors': serializer.errors})