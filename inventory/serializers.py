from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the Item model.

    This serializer handles the serialization and deserialization of Item instances,
    allowing for the conversion between Item objects and JSON representations.

    Fields:
        All fields from the Item model are included in the serialization process.
    """

    class Meta:
        model = Item
        fields = '__all__'  # Include all fields from the Item model
