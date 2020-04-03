from django.db import models

# Create your models here.
class Challenge(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.TextField()

    def __str__(self):
        return f'{self.image_url}{self.name}'

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.TextField()
    description = models.CharField(max_length=200)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='exercises')

    def __str__(self):
        return f'{self.name}{self.image}{self.description}'