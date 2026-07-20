from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.cars_listview),
    path('car/create/', views.cars_create),
    path('car/update/<int:pk>/', views.car_update),
    path('car/delete/<int:pk>/', views.cars_delete),
    path('car/<int:pk>/patch/', views.cars_patch),
]