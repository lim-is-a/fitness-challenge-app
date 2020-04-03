from django.contrib import admin

# Register your models here.
from .models import Challenge, Exercise

admin.site.register(Challenge)
admin.site.register(Exercise)