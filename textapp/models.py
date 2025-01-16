from django.db import models
import datetime


# Create your models here.
class TextInference(models.Model):
    originText = models.TextField()
    inferenceText = models.TextField()
    task_type = models.CharField(max_length=100)
    user_ip = models.CharField(max_length=100, default="-1.-1.-1.-1")
    update_time = models.DateTimeField(default=datetime.datetime.now())
