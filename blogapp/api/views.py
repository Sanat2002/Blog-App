from rest_framework import viewsets
from blogapp.models import blog,registration
from .serializers import BlogSerializer,RegistrationSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication

class RegistrationApi(viewsets.ModelViewSet):
    queryset = registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class BlogApi(viewsets.ModelViewSet):
    queryset = blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]