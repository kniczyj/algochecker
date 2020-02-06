from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=200, null=False)
    pub_date = models.DateField()
    exercise_text = RichTextUploadingField()

    # displays title instead of object in django admin
    def __str__(self):
        return self.exercise_name


class InputFile(models.Model):
    # m:1 with Exercise
    input = models.ForeignKey(Exercise, null=False,
                              on_delete=models.CASCADE)  # When a Case is deleted, upload models are also deleted
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return f"Input for exercise '{self.input.exercise_name}'"


class OutputFile(models.Model):
    # m:1 with Exercise
    input = models.ForeignKey(Exercise, null=False,
                              on_delete=models.CASCADE)  # When a Case is deleted, upload models are also deleted
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return f"Output for exercise '{self.input.exercise_name}'"
