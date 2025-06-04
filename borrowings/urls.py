from django.urls import path, include
from rest_framework import routers

from borrowings.views import BorrowingViewSet, BorrowingReturnViewSet

router = routers.DefaultRouter()
router.register("books", BorrowingViewSet, basename="borrowings")
router.register("return-book", BorrowingReturnViewSet, basename="return-book")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "borrowings"
