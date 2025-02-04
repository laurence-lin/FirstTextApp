from django.db import models
import datetime, zoneinfo
from django import utils



def get_taipei_time():
    # Define Default Timezone
    tzone = zoneinfo.ZoneInfo('Asia/Taipei')
    return utils.timezone.now().astimezone(tzone)

# Create your models here.
class TextInference(models.Model):
    originText = models.TextField()
    inferenceText = models.TextField()
    task_type = models.CharField(max_length=100)
    user_ip = models.CharField(max_length=100, default="-1.-1.-1.-1")
    update_time = models.DateTimeField(default=utils.timezone.now()) # Only store UTC time in database, translate to Custom timezone in Template or Form

