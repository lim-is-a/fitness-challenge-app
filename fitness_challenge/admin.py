from django.contrib import admin

# Register your models here.
from .models import Challenge, Exercise, Result

admin.site.register(Challenge)
admin.site.register(Exercise)
admin.site.register(Result)