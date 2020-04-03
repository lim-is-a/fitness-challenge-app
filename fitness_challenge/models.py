from django.db import models

# Create your models here.
class Challenge(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=500, null = True)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=500)
    description = models.CharField(max_length=200)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='exerciseList')

    def __str__(self):
        return f'{self.name}{self.image_url}{self.description}'