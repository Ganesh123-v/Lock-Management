from django.db import models
from main.models import User

# Create your models here.
class LockStation(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    # You can add other attributes as per your requirements

    def __str__(self):
        return self.name
    
class LockType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Lock(models.Model):
    STATUS_CHOICES = [
        ('RESERVED', 'Reserved'),
        ('RENTED', 'Rented'),
        ('AVAILABLE', 'Available'),
    ]
    
    lock_type = models.ForeignKey(LockType, on_delete=models.CASCADE)
    inner_height = models.IntegerField()
    inner_width = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='AVAILABLE')
    price = models.FloatField()
    station = models.ForeignKey(LockStation, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.lock_type.name
    
class Rental(models.Model):
    lock = models.ForeignKey(Lock, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.lock.lock_type.name + " - " + self.user.first_name + " " + self.user.last_name + " - " + str(self.start) + " - " + str(self.end)