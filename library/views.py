from rest_framework import viewsets, permissions
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
    serializer_class = BorrowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BorrowRecord.objects.filter(member__user=self.request.user)

    def perform_create(self, serializer):
        member = Member.objects.get(user=self.request.user)
        serializer.save(member=member)

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