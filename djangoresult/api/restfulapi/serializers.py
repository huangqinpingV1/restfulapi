#/usr/bin/env python 
#encoding:utf-8
#序列化模型为其他格式
from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music

        #序列化所有字段
        fields = '__all__'
        #序列化部分字段
        #fields = ('id','song','singer','last_modify_date','created')

