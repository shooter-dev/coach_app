from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


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

    seances = [
        {"date": "2025-07-10", "heure": "10:00", "objet": "Coaching motivation", "client": "alice", "note": "Bonne évolution"},
        {"date": "2025-07-15", "heure": "14:00", "objet": "Gestion du stress", "client": "bob", "note": ""},
    ]
    return render(request, 'dashboard/dashboard_coach.html', {'seances': seances})
