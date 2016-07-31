# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from main.models import Project, Picture
from main.serializers import ProjectSerializer, PictureSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# TODO: Revisar uso de Mixins
# http://www.django-rest-framework.org/tutorial/3-class-based-views/
class ProjectList(APIView):
    u"""
    Lista de todos los proyectos. Por ahora solo para obtener datos.
    """
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request, format=None):
        active = request.GET.get('active', None)
        projects = Project.objects.all()
        if active:
            projects = Project.objects.filter(active=active)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


# TODO: POST
class ProjectDetail(APIView):
    """
    Obtiene el detalle de un proyecto en particular.
    """
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
