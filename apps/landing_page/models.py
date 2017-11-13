# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

FEATURED = (
    ('featured', 'Featured'),
    ('hidden', 'Hidden'),
)


class Content(models.Model):
  title = models.CharField(max_length=120, default='Company Name')
  subtitle = models.TextField(max_length=1000, default='Subtitle')
  paragraph = models.TextField(max_length=1000, default='Description')
  input_placeholder = models.CharField(max_length=25, default='Email')
  button_placeholder = models.CharField(max_length=15, default='Submit')
  featured = models.CharField(
      max_length=20, choices=FEATURED, default='hidden')

  def __str__(self):
    return self.title
