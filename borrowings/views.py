from rest_framework import viewsets

from borrowings.models import Borrowing
from borrowings.serializer import BorrowingSerializer, BorrowingCreateSerializer


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return BorrowingCreateSerializer
        return BorrowingSerializer

    def get_queryset(self):
        return Borrowing.objects.filter(user=self.request.user)
