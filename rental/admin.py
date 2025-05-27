from django.contrib import admin
from .models import Lock, LockType, Rental

# Register your models here.
admin.site.register(LockType)
admin.site.register(Lock)
admin.site.register(Rental)