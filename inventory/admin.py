from django.contrib import admin

from inventory.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('name', 'category', 'quantity', 'price', 'created_at')

    # Add filters for the fields you want to filter by
    list_filter = ('category', 'created_at')

    # Enable search functionality for specific fields
    search_fields = ('name', 'category', 'description')

    # Fields displayed on the detailed page
    fields = ('name', 'description', 'quantity', 'price', 'category', 'created_at', 'updated_at')

    # Make created_at and updated_at read-only, as they shouldn't be edited
    readonly_fields = ('created_at', 'updated_at')
