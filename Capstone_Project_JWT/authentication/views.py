from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializers



class UserModelViewSet(ModelViewSet):

    serializer_class = UserSerializers
    queryset = User.objects.all()
    http_method_names = ["get", "post", "put", "patch", "delete"]

    

