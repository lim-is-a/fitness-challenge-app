from django.shortcuts import render

from .models import Challenge, Exercise
# Create your views here.

def challenge_list(request):
    challenges = Challenge.objects.all()
    return render(request, 'fitness_challenge/challenge_list.html', {'challenges': challenges})

def challenge_detail(request, pk):
    challenge = Challenge.objects.get(pk=pk)
    return render(request, 'fitness_challenge/challenge_detail.html', {'challenge': challenge})