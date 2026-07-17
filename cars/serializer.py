from rest_framework import serializers
from .models import Cars


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'
        read_only_fields = ['id','created_at','updated_at']