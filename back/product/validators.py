from rest_framework import serializers

from rest_framework.validators import UniqueValidator

from product.models import Product





def validate_title(value):
    value=str.title(value)
    qs= Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"This: {value} is already present")
    return value
 
def validate_title_2(value):
    if "hanuman" not in value.lower():
        raise serializers.ValidationError(f"Hanuman Ji needed in :{value}")
    return  value

unique_product_title=UniqueValidator(queryset=Product.objects.all(), lookup='iexact')