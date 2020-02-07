from django.contrib import admin
from .models import Exercise, InputFile, OutputFile


class InputFileInline(admin.TabularInline):
    model = InputFile


class OutputFileInline(admin.TabularInline):
    model = OutputFile


class InputOutputAdmin(admin.ModelAdmin):
    inlines = [InputFileInline, OutputFileInline]


admin.site.register(Exercise, InputOutputAdmin)
