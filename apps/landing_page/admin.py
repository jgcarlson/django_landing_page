# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Content

# Register your models here.


class ContentAdmin(admin.ModelAdmin):
  actions = ['make_featured']

  def make_featured(self, request, queryset):
    queryset.update(featured='featured')
  make_featured.short_description = "Choose template to display."


admin.site.register(Content)
