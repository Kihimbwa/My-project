from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, MemberViewSet, BorrowViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)
router.register(r'borrows', BorrowViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]