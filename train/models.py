from django.db import models

# Create your models here.


class Station(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Train(models.Model):
    origin = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name="arrival")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.origin} to {self.destination} in {self.duration} mins"
