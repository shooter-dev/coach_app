from django.db import models

from coachapp import settings


class Booking(models.Model):  # ou Booking
    date = models.DateField()
    heure_debut = models.TimeField()
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    objet = models.CharField(max_length=255)
    note_coach = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('date', 'heure_debut')  # pas de double réservation

    def __str__(self):
        return f"{self.date} {self.heure_debut} – {self.client.username}"

