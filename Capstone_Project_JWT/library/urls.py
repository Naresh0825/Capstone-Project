from rest_framework.routers import DefaultRouter
from .views import UserModelViewSet,BookViewSet,BorrowViewSet
from django.urls import path, include


router=DefaultRouter()

router.register(r'users', UserModelViewSet, basename="users")
router.register(r'books', BookViewSet, basename="books")
router.register(r'borrows', BorrowViewSet, basename="borrows")

urlpatterns = [path('', include(router.urls)),]