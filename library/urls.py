from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, MemberViewSet, BorrowViewSet, register_student, login_student, register_librarian

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)
router.register(r'borrows', BorrowViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', register_student, name='register_student'),
    path('api/register/librarian/', register_librarian, name='register_librarian'),
    path('api/login/', login_student, name='login_student'),
]
