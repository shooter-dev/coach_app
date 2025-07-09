from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
import calendar
from booking.models import Booking


@login_required
def dashboard_client_view(request):
    if request.user.is_coach:
        return redirect('dashboard_coach')

    # Données fictives (liste de dictionnaires)
    seances = [
        {"date": "2025-07-10", "heure": "10:00", "objet": "Coaching motivation"},
        {"date": "2025-07-15", "heure": "14:00", "objet": "Gestion du stress"},
    ]
    return render(request, 'dashboard/dashboard_client.html', {'seances': seances})

@login_required
def dashboard_coach_view(request):
    if not request.user.is_coach:
        return redirect('dashboard_client')

    # Récupération des paramètres dans l'URL
    month = request.GET.get('month')
    year = request.GET.get('year')

    today = timezone.now().date()
    month = int(month) if month else today.month
    year = int(year) if year else today.year

    # Gérer les dépassements d'année si nécessaire (ex: mois = 0 ou 13)
    if month < 1:
        month = 12
        year -= 1
    elif month > 12:
        month = 1
        year += 1

    bookings = Booking.objects.all()
    cal = calendar.Calendar(firstweekday=0)

    month_days = cal.itermonthdates(year, month)

    calendar_data = []

    for day in month_days:
        day_bookings = [b for b in bookings if b.date == day]
        calendar_data.append({
            'date': day,
            'bookings': day_bookings,
            'current_month': (day.month == month),
        })

    # Pour créer les liens vers les mois précédent et suivant
    prev_month = month - 1
    next_month = month + 1
    prev_year = year
    next_year = year

    if prev_month < 1:
        prev_month = 12
        prev_year -= 1

    if next_month > 12:
        next_month = 1
        next_year += 1

    return render(request, 'dashboard/dashboard_coach.html', {
        'calendar_data': calendar_data,
        'month_name': calendar.month_name[month],
        'month': month,
        'year': year,
        'day_names': ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"],
        'prev_month': prev_month,
        'prev_year': prev_year,
        'next_month': next_month,
        'next_year': next_year,
    })