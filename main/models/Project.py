# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from .Picture import Picture


class Project(models.Model):
    name = models.CharField('Project', max_length=120, null=False, blank=False)
    active = models.BooleanField('Active', default=False)
    start = models.DateField('Start', null=True, blank=True)
    end = models.DateField('End', null=True, blank=True)
    picture = models.ForeignKey(Picture, null=True, 
                                        related_name='picture_projects')
    thumbnail = models.ForeignKey(Picture, null=True, 
                                        related_name='thumbnail_projects')
    updated = models.DateTimeField('Updated', auto_now=True)
    created = models.DateTimeField('Created', auto_now_add=True)

    class Meta:
        app_label = 'main'

    def __unicode__(self):
        return self.name

