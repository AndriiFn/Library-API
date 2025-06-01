from rest_framework import viewsets, mixins

from borrowings.models import Borrowing
from borrowings.serializer import BorrowingSerializer


class BorrowingsListDetail(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
