from rest_framework import serializers
from .models import Rental, Lock, LockType
from main.models import User

class RentalSerializer(serializers.Serializer):
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()
    
    class Meta:
        fields=['start', 'end']
        
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        lock = self.context.get('lock')
        lock.status = 'RENTED'
        lock.save()
        rental = Rental.objects.create(start=validated_data.get('start'), end=validated_data.get('end'), lock=lock, user=user)
        return rental