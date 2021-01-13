from django.contrib import admin
from django.urls import path,include
from .views import PlantListCreateAPIView,PlantRetrieveAPIView,OrderListCreateAPIView

urlpatterns = [
    path("plant",PlantListCreateAPIView.as_view()),
    path("plant/<int:pk>",PlantRetrieveAPIView.as_view()),
    path("order",OrderListCreateAPIView.as_view()),
]