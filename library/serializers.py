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
    cover_image = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = '__all__'
    
    def get_cover_image(self, obj):
        if not obj.cover_image:
            return None
        # Always return just the relative URL path
        return obj.cover_image.url

class BorrowSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    member = MemberSerializer(read_only=True)
    book_id = serializers.IntegerField(write_only=True)
    expected_return_date = serializers.DateField()

    class Meta:
        model = BorrowRecord
        fields = ['id', 'book', 'member', 'book_id', 'borrow_date', 'expected_return_date', 'actual_return_date', 'penalty']
        read_only_fields = ['borrow_date', 'actual_return_date', 'penalty']
    
    def create(self, validated_data):
        book_id = validated_data.pop('book_id')
        book = Book.objects.get(id=book_id)
        return BorrowRecord.objects.create(book=book, **validated_data)
