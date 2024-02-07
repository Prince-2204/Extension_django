from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/submit-url/', views.submit_url, name='submit_url'),
]
