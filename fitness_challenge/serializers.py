from rest_framework import serializers
from .models import Challenge, Exercise

class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    exerciseList = serializers.HyperlinkedRelatedField(
        view_name = 'exercise_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Challenge
        fields = ('id', 'name', 'image_url', 'exerciseList')

class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    challenge = serializers.HyperlinkedRelatedField(
        view_name = 'challenge_detail', 
        many = False, 
        read_only = False, 
        queryset = Challenge.objects.all(),
    )
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'image_url', 'description', 'challenge')