from django.http import HttpResponse
from django.shortcuts import render

from .models import Train
from .models import Station
# Create your views here.


def index(request):
    context = {
        "trains": Train.objects.all(),
        "stations": Station.objects.all()
    }

    return render(request, "train/index.html", context)
