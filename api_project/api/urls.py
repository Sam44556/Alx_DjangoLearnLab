from django.urls import path,include
from .views import BookListCreateAPIView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'books', BookListCreateAPIView, basename='book')

urlpatterns = [
    path("api/",include(router.urls)),
]