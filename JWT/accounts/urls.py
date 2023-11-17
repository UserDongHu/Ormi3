# accounts/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import example_view

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path('join/', include("dj_rest_auth.registration.urls")),
    path('test/', example_view),
]