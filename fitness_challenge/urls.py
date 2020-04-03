from django.urls import path
from . import views

urlpatterns = [
    path('', views.challenge_list, name='challenge_list'),
    path('exercise/', views.exercise_list, name='exercise_list'),
]