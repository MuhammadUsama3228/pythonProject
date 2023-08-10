from django.db import models
from django.utils import timezone as tz


class Article(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(max_length=100, null=True)
    datetime = models.DateTimeField(default=tz.now)

    def __str__(self):
        return f'{self.title}'
