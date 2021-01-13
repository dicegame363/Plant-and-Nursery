from django.contrib import admin
from django.urls import path,include
from .views import UserAndNurseryCreateAPIView

urlpatterns = [
    path("register",UserAndNurseryCreateAPIView.as_view()),
]