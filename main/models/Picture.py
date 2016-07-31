# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Picture(models.Model):
    # TODO: Documentar
    # TODO: Metodo de resize
    SIZE_CHOICES = (
        ('x-large', 'x-large'),
        ('large', 'large'),
        ('medium', 'mediun'),
        ('small', 'small')
    )
    name = models.CharField('Project', max_length=120, null=False, blank=False)
    size = models.CharField('Size', max_length=10, choices=SIZE_CHOICES, 
                            default='small')
    file = models.ImageField('File', upload_to='pictures')
    height = models.IntegerField('Height', default=0, null=True, blank=True)
    width = models.IntegerField('Height', default=0, null=True, blank=True)
    updated = models.DateTimeField('Updated', auto_now=True)
    created = models.DateTimeField('Created', auto_now_add=True)

    class Meta:
        app_label = 'main'

    def __unicode__(self):
        return name
