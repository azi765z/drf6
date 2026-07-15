from django.db import models

# Create your models here.
class Cars(models.Model):
    model = models.CharField(max_length=100)
    mator = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model