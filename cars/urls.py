from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.CarsList.as_view()),
    path('car/create/', views.CarCreate.as_view()),
    path('car/update/<int:pk>/', views.CarUpdate.as_view()),
    path('car/delete/<int:pk>/', views.CarDelete.as_view()),
    path('car/<int:pk>/', views.CarUpdateDestroyAPIView.as_view()),
]