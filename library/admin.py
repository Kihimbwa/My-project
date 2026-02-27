from django.contrib import admin
from .models import Book, Member, BorrowRecord


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre", "available_copies", "display_cover_image")
    search_fields = ("title", "author")
    list_filter = ("genre", "publication_date")
    
    # Method to display cover image thumbnail in list view
    def display_cover_image(self, obj):
        if obj.cover_image:
            from django.utils.html import format_html
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.cover_image.url)
        return "No Image"
    
    display_cover_image.short_description = "Cover Image"


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("member_id", "user", "phone")
    search_fields = ("member_id", "user__username", "user__first_name", "user__last_name")


@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'borrow_date', 'actual_return_date', 'penalty')
    list_filter = ('borrow_date', 'actual_return_date')
    search_fields = ('book__title', 'member__user__username', 'member__member_id')
