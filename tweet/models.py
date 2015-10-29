
from django.db import models
from core.models import TimeStampedModel
from django.conf import settings


class Tweet(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.CharField(max_length=140)

    class Meta:
        ordering = ['-created_at']

    def __unicode__(self):
        return self.text