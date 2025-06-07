from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.Serializer):
    class Meta:
        model = Payment
        fields = ("id", "status", "type", "borrowing_id", "session_url", "session_id", "money_to_pay")


class PaymentListSerializer(PaymentSerializer):
    class Meta:
        model = Payment
        fields = ("id", "status", "type", "money_to_pay")


class PaymentDetailSerializer(PaymentSerializer):
    class Meta:
        model = Payment
        fields = ("id", "status", "type", "borrowing_id", "session_url", "session_id", "money_to_pay")
