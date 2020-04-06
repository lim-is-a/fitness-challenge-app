from django.urls import path
from . import views

urlpatterns = [
    path('', views.challenge_list, name='challenge_list'),
    path('challenges/<int:pk>', views.challenge_detail, name='challenge_detail'),
    path('challenges/new', views.challenge_create, name='challenge_create'),
    path('challenges/<int:pk>/edit', views.challenge_edit, name='challenge_edit'),
    path('exerciseList/new', views.exercise_create, name='exercise_create'),
    # path('exerciseList/<int:pk>/edit', views.exercise_edit, name='exercise_edit'),
]
