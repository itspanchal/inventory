from django.db import models


class BaseModal(models.Model):
    """
    An abstract base model that provides common fields for all models.

    Fields:
        is_active (bool): Indicates whether the record is active. Defaults to True.
        created_at (datetime): The timestamp when the record was created. Automatically set on creation.
        updated_at (datetime): The timestamp when the record was last updated. Automatically updated on save.
    """
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Item(BaseModal):
    """
    Model representing an inventory item.

    Inherits from BaseModal to include common fields.

    Fields:
        name (str): The name of the item. Max length of 255 characters.
        description (str): A brief description of the item. Optional.
        quantity (int): The quantity of the item available in inventory. Defaults to 1000.
        price (Decimal): The price of the item. Max digits of 10, with 2 decimal places. Defaults to 20.
        category (str): The category the item belongs to. Optional.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=20)
    category = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        """Return a string representation of the item, which is its name."""
        return self.name
