from django.db import models


class Cars(models.Model):
    brand = models.CharField(max_length=100)      
    model = models.CharField(max_length=100)      
    color = models.CharField(max_length=50)
    year = models.PositiveIntegerField(default=2023)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    fuel_type = models.CharField(max_length=50)   
    image = models.ImageField(upload_to="cars/", blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.model}"