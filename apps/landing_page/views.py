# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import View, CreateView
from django.shortcuts import render
from .models import Content

# Create your views here.


class IndexView(CreateView):
  template_name = 'landing_page/index.html'
  model = Content
  fields = '__all__'

  def get_context_data(self, *args, **kwargs):
    context = super(IndexView, self).get_context_data(*args, **kwargs)
    context['obj'] = Content.objects.filter(featured='featured').first()
    return context
