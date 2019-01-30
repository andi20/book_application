from __future__ import unicode_literals

from django.db import models
from django.shortcuts import reverse


# Create your models here.
# publisher model with its attributes
class Publisher(models.Model):
    Author = models.CharField(max_length=30)
    Book = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)

    def __unicode__(self):
        return self.Author

    def get_post_url(self):
        return reverse('update_publisher', kwargs={'pk': self.pk})
