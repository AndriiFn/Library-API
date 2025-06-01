from django.urls import path, include
from rest_framework import routers

from borrowings.views import BorrowingsListDetail

router = routers.DefaultRouter()
router.register("books", BorrowingsListDetail)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "borrowings"
