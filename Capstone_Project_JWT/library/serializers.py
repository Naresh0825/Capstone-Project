from rest_framework import serializers
from .models import User, Book, Borrow

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class BorrowSerializers(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = "__all__"
