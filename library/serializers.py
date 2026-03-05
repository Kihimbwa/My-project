from rest_framework import serializers
from .models import Book, Member, BorrowRecord
from django.contrib.auth.models import User
from django.conf import settings

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
        if obj.cover_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.cover_image.url)
            # Fallback: construct URL manually
            return f"{settings.MEDIA_URL}{obj.cover_image.url}"
        return None

class BorrowSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    member = MemberSerializer(read_only=True)
    book_id = serializers.IntegerField(write_only=True)  # Changed to IntegerField
    expected_return_date = serializers.DateField()

    class Meta:
        model = BorrowRecord
        fields = ['id', 'book', 'member', 'book_id', 'borrow_date', 'expected_return_date', 'actual_return_date', 'penalty']
        read_only_fields = ['borrow_date', 'actual_return_date', 'penalty']
    
    def create(self, validated_data):
        # Get the book by ID
        book_id = validated_data.pop('book_id')
        book = Book.objects.get(id=book_id)
        
        # Create the borrow record with the book object
        return BorrowRecord.objects.create(book=book, **validated_data)
