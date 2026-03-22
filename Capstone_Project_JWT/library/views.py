from rest_framework.viewsets import ModelViewSet
from .models import User, Book, Borrow
from .serializers import UserSerializers, BookSerializers, BorrowSerializers

class UserModelViewSet(ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    http_method_names = ["get", "post"]
    serializer_class = UserSerializers

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    http_method_names=  ["get", "post"]
    serializer_class = BookSerializers

class BorrowViewSet(ModelViewSet):
    queryset = Borrow.objects.all()
    http_method_names = ["get", "post"]
    serializer_class = BorrowSerializers
