from django.urls import path
from . import views

urlpatterns = [
    path('', views.challenge_list, name='challenge_list'),
    path('challenges/<int:pk>', views.challenge_detail, name='challenge_detail'),
    path('challenges/new', views.challenge_create, name='challenge_create'),
    path('exerciseList/new', views.exercise_create, name='exercise_create'),
]
