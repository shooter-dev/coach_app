from django.contrib.auth.models import User
from django.db import models


class Availability(models.Model):
    day_name = models.CharField(max_length=10)  # ex: 'Lundi'
    hour = models.TimeField()

    class Meta:
        unique_together = ("day_name", "hour")
        ordering = ["day_name", "hour"]

    def __str__(self):
        return f"{self.day_name} à {self.hour}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    note = models.TextField(blank=True, null=True)  # Notes coach uniquement

    class Meta:
        unique_together = ('date',)
        ordering = ['date']

    def __str__(self):
        return f"RDV de {self.user.username} le {self.date}"