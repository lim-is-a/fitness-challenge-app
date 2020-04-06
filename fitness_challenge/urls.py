from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('challenges', views.ChallengeView)
router.register('exerciseList', views.ExerciseView)
router.register('results', views.ResultView)

urlpatterns = [
    path('', include(router.urls)),
]
