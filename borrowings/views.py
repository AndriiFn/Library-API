from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from borrowings.models import Borrowing
from borrowings.permissions import IsAdminOrIfAuthenticatedReadOnly
from borrowings.serializer import (
    BorrowingSerializer,
    BorrowingCreateSerializer,
    BorrowingReturnSerializer
)


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.select_related("user", "book").all()
    serializer_class = BorrowingSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly, )

    def get_serializer_class(self):
        if self.action == "create":
            return BorrowingCreateSerializer
        return BorrowingSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Borrowing.objects.all()

        return Borrowing.objects.filter(user=self.request.user)


class BorrowingReturnViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingReturnSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        if self.request.user.is_staff:
            return Borrowing.objects.all()

        return Borrowing.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        borrowing = self.get_object()
        serializer = self.get_serializer(borrowing, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
