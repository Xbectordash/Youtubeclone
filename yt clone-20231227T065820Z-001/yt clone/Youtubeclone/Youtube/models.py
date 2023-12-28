from django.db import models

# Create your models here.
class yt_attribute(models.Model):

    Thumbnail = models.ImageField(upload_to='pics')
    video_time = models.TimeField()
    channel_pic = models.ImageField(upload_to='pics')
    video_title = models.CharField(max_length=200)
    channel_name = models.CharField(max_length=200)
    views = models.FloatField()
    days = models.IntegerField()

    # Thumbnail: str
    # video_time: str
    # channel_pic : str
    # video_title: str
    # channel_name: str
    # views: float
    # days: int

# learn django model field type
#install Pillow for image migrations
