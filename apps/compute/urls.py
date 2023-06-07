from django.urls import path
from .views import compute_fibonacci


app_name = "compute"

urlpatterns = [
    path("fibonacci", view=compute_fibonacci, name="compute_fibonacci"),
]
