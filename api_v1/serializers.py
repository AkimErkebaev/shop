from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from webapp.models import Product, Order, OrderProduct


class ProductModelsSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print(instance)

        return data

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")

    def validate_title(self, value):
        if len(value) < 5:
            raise ValidationError("Длина маленькая")
        return value


class OrderModelsSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print(instance)

        return data

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ("id", "created_at", "user")

    def validate_title(self, value):
        if len(value) < 5:
            raise ValidationError("Длина маленькая")
        return value


class OrderProductModelsSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print(instance)

        return data

    class Meta:
        model = OrderProduct
        fields = "__all__"
        read_only_fields = ("id", "created_at")

    def validate_title(self, value):
        if len(value) < 5:
            raise ValidationError("Длина маленькая")
        return value
