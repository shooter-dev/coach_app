from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from booking.models import Booking


class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_display = ['date', 'heure_debut', 'client', 'objet', 'note_coach']

admin.site.register(Booking, BookingAdmin)