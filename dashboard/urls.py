from django.urls import path
from . import views

urlpatterns = [
    path("client/planning", views.client_planning, name="client_planning"),
    path("client/history", views.client_history, name="client_history"),
    path("coach/planning", views.coach_planning, name="coach_planning"),
    path("coach/horaire", views.coach_availability, name="coach_availability"),
]
