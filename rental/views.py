from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Lock, Rental, LockStation
from .serializers import RentalSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.

def locks(request):
    event_list = Lock.objects.filter(status="AVAILABLE")
    paginator = Paginator(event_list, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'locks.html', {'page_obj': page_obj})

def stations(request):
    stations = LockStation.objects.all()
    paginator = Paginator(stations, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'stations.html', {'page_obj': page_obj})

@login_required(login_url="/user/login")
def rentals(request):
    rentals = Rental.objects.filter(user=request.user)
    paginator = Paginator(rentals, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'rentals.html', {'page_obj': page_obj})

@login_required(login_url="/user/login")
def create_rental(request, lock_id):
    try:
        lock = Lock.objects.get(id=lock_id)
        
        if request.method == "POST":
            if lock .status == 'RENTED':
                return render(request, 'create_rental_form.html', {'lock': lock, 'alert': { 'show': True, 'severity': 'warning', 'message': f"This lock has already been rented" }})
            serializer = RentalSerializer(data=request.POST, context={'request': request, 'lock': lock})
            if serializer.is_valid():
                serializer.save()
                return render(request, 'create_rental_form.html', {'lock': lock, 'alert': { 'show': True, 'severity': 'success', 'message': f"You have succesfully acquired access to the {lock}" }})
            else:
                errors = serializer.errors
                return render(request, 'create_rental_form.html', {'lock': lock, 'alert': { 'show': True, 'severity': 'danger', 'message': ".\t".join([f"{error} - {''.join(errors[error])}" for error in errors]) }})
    except Lock.DoesNotExist:
        lock = None
    return render(request, 'create_rental_form.html', {'lock': lock})