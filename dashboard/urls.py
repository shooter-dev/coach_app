from django.urls import path
from .views import dashboard_client_view, dashboard_coach_view

urlpatterns = [
    path('client/', dashboard_client_view, name='dashboard_client'),
    path('coach/', dashboard_coach_view, name='dashboard_coach'),
]