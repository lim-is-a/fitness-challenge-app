from django import forms
from .models import Challenge, Exercise, Result

class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ('name', 'image_url')

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('challenge','name', 'image_url', 'description')

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('challenge_name', 'name', 'date', 'time', 'avg_hr','max_hr', 'cals_burned', 'note')
