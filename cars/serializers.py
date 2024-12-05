from rest_framework import serializers
from .models import Cars

class CarsSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Cars
         # field = ('id', 'name',)
        fields = '__all__'
