from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.stations, name="stations"),
    path('locks', views.locks, name="locks"),
    path('rentals', views.rentals, name="rentals"),
    path('create_rental/<lock_id>', views.create_rental, name="create_rental")
]