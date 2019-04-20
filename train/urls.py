from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:train_id>", views.train_id, name="train_id")
]
