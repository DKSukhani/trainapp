from django.contrib import admin
from . import models


# Register your models here.

admin.site.register(models.Train)
admin.site.register(models.Station)
admin.site.register(models.Passenger)
