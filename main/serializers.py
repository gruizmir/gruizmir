# -*- coding: utf-8 -*-
from main.models import Picture, Project
from rest_framework import serializers


class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture


class ProjectSerializer(serializers.ModelSerializer):
    picture = PictureSerializer()
    thumbnail = PictureSerializer()
    
    class Meta:
        model = Project
