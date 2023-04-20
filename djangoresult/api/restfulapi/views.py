#/usr/bin/env python
#encoding:utf-8
from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser
from .models import Music
from .serializers import MusicSerializer
from django_filters import rest_framework as filters
from utils.CustomViewBase import *
# Create your views here.
class MusicViewSet(CustomViewBase):
    """
    CURD功能
    """
    authentication_classes = []
    permission_classes =[]

    #解析方式
    parse_classes = (MultiPartParser,FormParser,JSONParser)

    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    def create(self,request,*args,**kwargs):
        """creat music"""
        return super().create(request,*args,**kwargs)
    
    def list(self,request,*args,**kwargs):
        """all music"""
        print("list() enter")
        return super().list(request,*args,**kwargs)

    def retrieve(self,request,*args,**kwargs):
        """查询一条数据"""
        return super().retrieve(requst,*args,**kwargs)

    def update(self,request,*args,**kwargs):
        """更新一条数据"""
        return super().update(request,*args,**kwargs)
    
    def destroy(self,request,*args,**kwargs):
        """删除一条数据"""
        return super().destroy(request,*args,**kwargs)


