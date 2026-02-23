from rest_framework import serializers
from .models import Book, Member, BorrowRecord
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Member
        fields = ['id', 'member_id', 'phone', 'address', 'role', 'user']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    member = MemberSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), source='book', write_only=True)
    member_id = serializers.PrimaryKeyRelatedField(queryset=Member.objects.all(), source='member', write_only=True)

    class Meta:
        model = BorrowRecord
        fields = ['id', 'book', 'member', 'book_id', 'member_id', 'borrow_date', 'expected_return_date', 'actual_return_date', 'penalty']
