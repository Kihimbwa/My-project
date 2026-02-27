from rest_framework import viewsets, permissions, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Book, Member, BorrowRecord
from .serializers import BookSerializer, MemberSerializer, BorrowSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated]

class BorrowViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BorrowRecord.objects.filter(member__user=self.request.user)

    def perform_create(self, serializer):
        try:
            member = Member.objects.get(user=self.request.user)
            book = serializer.validated_data.get('book')
            
            # Check if book is available
            if book.available_copies < 1:
                raise serializers.ValidationError({'error': 'No copies available'})
            
            # Decrease available copies
            book.available_copies -= 1
            book.save()
            
            serializer.save(member=member)
        except Member.DoesNotExist:
            raise serializers.ValidationError({'error': 'Member profile not found. Please contact the librarian.'})

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        borrow = self.get_object()
        borrow.actual_return_date = timezone.now().date()
        if borrow.actual_return_date > borrow.expected_return_date:
            days_late = (borrow.actual_return_date - borrow.expected_return_date).days
            borrow.penalty = days_late * 1000
        borrow.book.available_copies += 1
        borrow.book.save()
        borrow.save()
        serializer = self.get_serializer(borrow)
        return Response(serializer.data)

# Student Registration View
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_student(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    phone = request.data.get('phone')
    address = request.data.get('address')
    
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)
    
    # Create user
    user = User.objects.create_user(username=username, email=email, password=password)
    
    # Generate unique member_id
    import random
    member_id = 'STU' + str(random.randint(10000, 99999))
    
    # Create member profile
    member = Member.objects.create(
        user=user,
        member_id=member_id,
        phone=phone,
        address=address,
        role='student'
    )
    
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({
        'message': 'Student registered successfully',
        'member_id': member_id,
        'token': token.key
    }, status=201)

# Student Login View
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_student(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user:
        token, created = Token.objects.get_or_create(user=user)
        try:
            member = Member.objects.get(user=user)
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'member_id': member.member_id,
                'role': member.role
            })
        except Member.DoesNotExist:
            return Response({'error': 'Member profile not found'}, status=400)
    
    return Response({'error': 'Invalid credentials'}, status=400)

# Librarian Registration View
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_librarian(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    phone = request.data.get('phone')
    address = request.data.get('address')
    
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)
    
    # Create user
    user = User.objects.create_user(username=username, email=email, password=password)
    
    # Generate unique member_id for librarian
    import random
    member_id = 'LIB' + str(random.randint(10000, 99999))
    
    # Create member profile with librarian role
    member = Member.objects.create(
        user=user,
        member_id=member_id,
        phone=phone,
        address=address,
        role='librarian'
    )
    
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({
        'message': 'Librarian registered successfully',
        'member_id': member_id,
        'token': token.key
    }, status=201)
