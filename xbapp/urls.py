# -*- coding: utf-8 -*-
from django.conf.urls import patterns,url, include

urlpatterns = patterns('xbapp.views',
    url(r'^$', 'inicio'),
)