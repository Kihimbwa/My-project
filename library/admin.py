from django.contrib import admin
from .models import Book, Member, BorrowRecord


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre", "available_copies")
    search_fields = ("title", "author")
    list_filter = ("genre", "publication_date")


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("member_id", "user", "phone")
    search_fields = ("member_id", "user__username", "user__first_name", "user__last_name")


class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'borrow_date', 'actual_return_date', 'penalty')
    list_filter = ('borrow_date', 'actual_return_date')
