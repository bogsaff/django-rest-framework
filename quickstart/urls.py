from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('hello/', views.HelloAPIView.as_view(), name='hello'),
]
