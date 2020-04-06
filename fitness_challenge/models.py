from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Challenge(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=500, null = True)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=500)
    description = models.CharField(max_length=700)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='exerciseList')

    def __str__(self):
        return f'{self.name}{self.image_url}{self.description}'

class Result(models.Model):
    challenge_name = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='challengeResult')
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now=False)
    time = models.DurationField()
    avg_hr = models.IntegerField(validators=[MinValueValidator(30), MaxValueValidator(300)], null = True)
    max_hr = models.IntegerField(validators=[MinValueValidator(30), MaxValueValidator(300)], null= True)
    cals_burned = models.IntegerField(null = True)
    note = models.CharField(max_length=1000)

    def __str__(self):

        return f'{self.name}{self.challenge_name}{self.time}'