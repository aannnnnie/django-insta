from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class PhotoPost(models.Model):
    author = models.ForeignKey(User)
    image = models.ImageField(upload_to='images')
    description = models.TextField()

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return "%s:%s" % (self.author.username, self.image.name)

