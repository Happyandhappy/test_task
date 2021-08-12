from django.db import models


# Create your models here.


class Tweet(models.Model):
    name = models.CharField('name', max_length=50)
    message = models.CharField('tweet message', max_length=50)
    create_at = models.DateTimeField('timestamp', auto_now_add=True)

