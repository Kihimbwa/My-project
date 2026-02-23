from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    genre = models.CharField(max_length=50)
    available_copies = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class Member(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('librarian', 'Librarian'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member_id = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return self.user.username

class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    penalty = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.member} borrowed {self.book}"