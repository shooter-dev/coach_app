# booking/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Booking, Availability
from .forms import BookingForm
from django.utils import timezone

def is_client(user):
    return user.groups.filter(name="Client").exists()

@login_required
@user_passes_test(is_client)
def add_booking(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            date = booking.date
            day = date.date()
            hour = date.time()

            # Vérifie que l'horaire est disponible
            if not Availability.objects.filter(day=day, hour=hour).exists():
                form.add_error("date", "Le créneau sélectionné n’est pas disponible.")
            elif Booking.objects.filter(date=date).exists():
                form.add_error("date", "Ce créneau est déjà pris.")
            else:
                booking.save()
                return redirect("client_planning")
    return render(request, "booking/prise_rdv_form.html", {"form": form, "title": "Prendre un rendez-vous"})

@login_required
@user_passes_test(is_client)
def update_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    form = BookingForm(instance=booking)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            new_date = form.cleaned_data['date']
            if Booking.objects.exclude(pk=pk).filter(date=new_date).exists():
                form.add_error("date", "Ce créneau est déjà réservé.")
            else:
                booking.date = new_date
                booking.save()
                return redirect("client_planning")
    return render(request, "booking/prise_rdv_form.html", {"form": form, "title": "Modifier le rendez-vous"})

@login_required
@user_passes_test(is_client)
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == "POST":
        booking.delete()
        return redirect("client_planning")
    return render(request, "booking/delete_confirm.html", {"booking": booking})
