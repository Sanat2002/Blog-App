from rest_framework import viewsets
from blogapp.models import blog,registration
from .serializers import BlogSerializer,RegistrationSerializer

class RegistrationApi(viewsets.ModelViewSet):
    queryset = registration.objects.all()
    serializer_class = RegistrationSerializer

class BlogApi(viewsets.ModelViewSet):
    queryset = blog.objects.all()
    serializer_class = BlogSerializer