from rest_framework import viewsets

from payment.models import Payment
from payment.serializer import PaymentListSerializer, PaymentDetailSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return PaymentListSerializer
        else:
            return PaymentDetailSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Payment.objects.all()

        return Payment.objects.filter(user=self.request.user)
