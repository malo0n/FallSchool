from django.urls import path
from . import views

urlpatterns = [
    path('first__screen/', views.first__screen, name='first__screen'),
    path('second__screen/', views.second__screen, name='second__screen')
]