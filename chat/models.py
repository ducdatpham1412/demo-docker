from django.db import models


class Chat(models.Model):
    type = models.IntegerField(default=0)
    content = models.TextField(default='')
