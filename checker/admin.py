from django.contrib import admin
from .models import Exercise, InputFile, OutputFile

# Register your models here.
admin.site.register(Exercise)
admin.site.register(InputFile)
admin.site.register(OutputFile)
