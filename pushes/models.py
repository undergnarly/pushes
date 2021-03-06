from django.conf import settings
from django.db import models
from django.utils import timezone


class Pushes(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(blank=False)


    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Options(models.Model):
    title = models.CharField(max_length=50)
    value = models.BooleanField(blank=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
