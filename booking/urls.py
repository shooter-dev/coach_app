# booking/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_booking, name="add_booking"),
    path("update/<int:pk>", views.update_booking, name="update_booking"),
    path("delete/<int:pk>", views.delete_booking, name="delete_booking"),
]
