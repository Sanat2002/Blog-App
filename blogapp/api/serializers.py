from django.db import models
from rest_framework import serializers
from blogapp.models import registration

from blogapp.models import blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = "__all__"

class RegistrationSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many=True,read_only=True)
    class Meta:
        model = registration
        fields = ['id','name','email','address','country','state','fi_password','se_password','phone','gender','choices','is_tick','auth_token','verified','blogs']