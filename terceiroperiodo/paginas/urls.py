from django.urls import path
from . views import indexView

urlpatter00ns=[
    path("inicio/", indexView.as_view(), name="inicio"),
    ]