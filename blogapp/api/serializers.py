from rest_framework import serializers
from blogapp.models import registration,blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = "__all__"

class RegistrationSerializer(serializers.ModelSerializer):
    # this will show that which blogs are written by the current user
    blogs = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = registration
        fields = ['id','name','email','address','country','state','fi_password','se_password','phone','gender','is_tick','auth_token','verified','blogs']