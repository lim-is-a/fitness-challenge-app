from django import forms
from .models import Challenge, Exercise

class ChallengeForm(forms.ModelForm):

    class Meta:
        model = Challenge
        fields = ('name', 'image_url')

class ExerciseForm(forms.ModelForm):

    class Meta:
        model = Exercise
        fields = ('name', 'image_url', 'description', 'challenge')