# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from main.views import ProjectList, ProjectDetail


urlpatterns = [
    url(r'^project/$', ProjectList.as_view()),
    url(r'^project/(?P<pk>[0-9]+)/$', ProjectDetail.as_view())
]
