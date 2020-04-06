from rest_framework import serializers
from .models import Challenge

class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    exerciseList = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True
    )
class Meta:
    model = Challenge
    fields = ('id', 'name', 'image_url', 'exerciseList')
