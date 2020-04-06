from rest_framework import serializers
from .models import Challenge, Exercise, Result


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'image_url', 'description', 'challenge')

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'challenge_name', 'name', 'date', 'time', 'avg_hr','max_hr', 'cals_burned', 'note')

class ChallengeSerializer(serializers.ModelSerializer):
    exerciseList = ExerciseSerializer(many=True, read_only=True)
    class Meta:
        model = Challenge
        fields = ('id', 'name', 'image_url', 'exerciseList')