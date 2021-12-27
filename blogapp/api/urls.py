from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('regisapi/',views.RegistrationApi,basename='regis')
router.register('blogapi/',views.BlogSerializer,basename='blog')

urlpatterns = [
    path('',include(router.urls))
]