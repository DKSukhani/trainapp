from django.http import HttpResponse, Http404
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


def train_id(request, train_id):
    try:
        train = Train.objects.get(id=train_id)
        train_id = train_id
    except Train.DoesNotExist:
        raise Http404("Train does not exist")
    context = {
        "train": train,
        "train_id": train_id
    }
    return render(request, "train/train_id.html", context)
