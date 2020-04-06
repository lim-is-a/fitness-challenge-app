from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    path('challenges', views.ChallengeList.as_view(), name='challenge_list'),
    path('challenges/<int:pk>', views.ChallengeDetail.as_view(), name='challenge_detail'),
    path('exerciseList', views.ExerciseList.as_view(), name='exercise_list'),
    path('exerciseList/<int:pk>', views.ExerciseDetail.as_view(), name='exercise_detail'),
]
