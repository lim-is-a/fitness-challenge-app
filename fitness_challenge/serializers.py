from rest_framework import serializers
from .models import Challenge, Exercise

class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    exerciseList = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True
    )
    class Meta:
        model = Challenge
        fields = ('id', 'name', 'image_url', 'exerciseList')

class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    challenge = serializers.HyperlinkedRelatedField(
        view_name = challenge_detail, 
        many = False, 
        read_only = True, 
        queryset = Challenge.objects.all(),
    )
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'image_url', 'description', 'challenge', 'challenge')