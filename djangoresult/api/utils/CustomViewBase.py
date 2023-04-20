#!/usr/bin/env python
#encoding:utf-8
from django_filters import rest_framework
from rest_framework import filters
from rest_framework import status
from rest_framework import viewsets
from .JsonResponse import JsonResponse
from django.http import HttpResponse

class CustomViewBase(viewsets.ModelViewSet):
    queryset =''
    serializer_class = ''
    permission_classes = ()
    filter_fields =()
    search_fileds =()

    filter_backends = (rest_framework.DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,)


    def create(self,request,*args,**kwargs):
        serializer =self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        headers = self.get_success_header(serializer.data)
        return JsonResponse(data=serializer.data,msg='success',code  =201,status  =status.HTTP_201_CREATED,headers =headers)

    def list(self,request,*args,**kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer =self.get_serializer(page,many=True)
            return self.get_paginate_response(serializer.data)
        serializer = self.get_serializer(queryset,many = True)
        print("CustomViewBase list() enter data = "+str(serializer.data))
        response = JsonResponse(data=serializer.data,code = 200,msg="success",status = status.HTTP_200_OK)
        print(isinstance(response,HttpResponse))
        return response


    def retrieve(self,request,*args,**kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(data=serializer.data,code =200,msg="success",status=status.HTTP_200_OK)

    def update(self,request,*args,**kwargs):
        partial = kwargs.pop('partial',False)
        instancce = self.get_object()
        serializer = self.get_serializer(instance,data=request.data,partial=partial)
        self.perform_update(serializer)

        if getattr(instance,'_prefetched_objects_cache',None):
            instance._prefetched_objects_cache = {}

        return JsonResponse(data=serializer.data,msg="success",code =200,status=status.HTTP_200_OK)


    def Destroy(self,request,*args,**kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return JsonResponse(data=[],code =204,msg="delete resouce success",status=status.HTTP_204_NO_CONTENT)


