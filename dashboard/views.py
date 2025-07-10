# dashboard/views.py
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.utils.dateparse import parse_time
from django.contrib import messages

from booking.models import Booking, Availability


def is_client(user):
    return user.groups.filter(name="Client").exists()

def is_coach(user):
    return user.groups.filter(name="Coach").exists()

@login_required
@user_passes_test(is_client)
def client_planning(request):
    upcoming = Booking.objects.filter(user=request.user, date__gte=now()).order_by("date")
    return render(request, "dashboard/client_planning.html", {"appointments": upcoming})

@login_required
@user_passes_test(is_client)
def client_history(request):
    past = Booking.objects.filter(user=request.user, date__lt=now()).order_by("-date")
    return render(request, "dashboard/client_history.html", {"appointments": past})

@login_required
@user_passes_test(is_coach)
def coach_planning(request):
    all_appointments = Booking.objects.select_related("user").order_by("date")
    return render(request, "dashboard/coach_planning.html", {"appointments": all_appointments})


@login_required
@user_passes_test(is_coach)
def coach_availability(request):
    days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    hours = [f"{h:02d}:00" for h in range(8, 19)]

    if request.method == "POST":
        selected = request.POST.getlist("availability")
        Availability.objects.all().delete()
        for entry in selected:
            day, hour = entry.split("|")
            Availability.objects.get_or_create(day_name=day, hour=hour)
        messages.success(request, "Disponibilités mises à jour.")
        return redirect("coach_availability")

    # Construire un set des disponibilités actuelles pour comparaison dans le template
    selected_slots = set(
        f"{a.day_name}|{a.hour.strftime('%H:%M')}" for a in Availability.objects.all()
    )

    return render(request, "dashboard/coach_availability.html", {
        "days": days,
        "hours": hours,
        "selected_slots": selected_slots,
    })
