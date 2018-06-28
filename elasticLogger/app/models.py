# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField(blank=True, default='')

    class Meta:
        ordering = ('created',)