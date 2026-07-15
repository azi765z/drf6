from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view()),
    path('products/create/', views.Postcreate.as_view()),
    path('products/update/<int:pk>/', views.PostUpdate.as_view()),
    path('products/delete/<int:pk>/', views.ProductDelete.as_view()),
    path('products/<int:pk>/', views.ProductsUpdateDestroyAPIView.as_view()),
]
