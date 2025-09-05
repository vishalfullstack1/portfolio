from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),   # 👈 yaha name diya hai
]
