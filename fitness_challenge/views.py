from django.shortcuts import render, redirect

from .models import Challenge, Exercise
from .forms import ChallengeForm, ExerciseForm
# Create your views here.

def challenge_list(request):
    challenges = Challenge.objects.all()
    return render(request, 'fitness_challenge/challenge_list.html', {'challenges': challenges})

def challenge_detail(request, pk):
    challenge = Challenge.objects.get(pk=pk)
    return render(request, 'fitness_challenge/challenge_detail.html', {'challenge': challenge})

def challenge_create(request):
    if request.method == 'POST':
        form = ChallengeForm(request.POST)
        if form.is_valid():
            challenge = form.save()
            return redirect('challenge_detail', pk=challenge.pk)
    else:
        form = ChallengeForm()
    return render(request, 'fitness_challenge/challenge_form.html', {'form': form})

def exercise_create(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save()
            return redirect('challenge_detail', pk=challenge.pk)
    else:
        form = ExerciseForm()
    return render(request, 'fitness_challenge/exercise_form.html', {'form': form})

def challenge_edit(request, pk):
    challenge = Challenge.objects.get(pk=pk)
    if request.method == "POST":
        form = ChallengeForm(request.POST, instance=challenge)
        if form.is_valid():
            challenge = form.save()
            return redirect('challenge_detail', pk=challenge.pk)
    else:
        form = ChallengeForm(instance=challenge)
    return render(request, 'fitness_challenge/challenge_form.html', {'form': form})

def exercise_edit(request, pk):
    exercise = Exercise.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            exercise = form.save()
            return redirect('challenge_detail', pk=exercise.challenge.pk)
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'fitness_challenge/exercise_form.html', {'form': form})
