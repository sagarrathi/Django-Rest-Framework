
from rest_framework import serializers
from product.models import Product





def validate_title(value):
    value=str.title(value)
    qs= Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"This: {value} is already present")
    return value
