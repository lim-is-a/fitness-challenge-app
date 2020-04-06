from rest_framework import viewsets
from .serializers import ChallengeSerializer, ExerciseSerializer, ResultSerializer
from .models import Challenge, Exercise, Result

class ChallengeView(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

class ExerciseView(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class ResultView(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

