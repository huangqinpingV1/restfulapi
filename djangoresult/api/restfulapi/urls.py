#!/usr/bin/env python 
#encoding:utf-8
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('music',views.MusicViewSet)
urlpatterns  =[
        path('',include(router.urls)),
        ]
