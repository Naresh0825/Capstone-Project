from rest_framework.routers import DefaultRouter
from .views import UserModelViewSet
from django.urls import path, include


router=DefaultRouter()

router.register(r'users', UserModelViewSet)

urlpatterns = [path('', include(router.urls)),]