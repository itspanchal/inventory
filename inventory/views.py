import logging

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response
from django.core.cache import cache

logger = logging.getLogger('inventory')


class ItemCreateView(generics.CreateAPIView):
    """
    API view to create a new item.

    This view handles the creation of an Item instance. It checks if the item
    with the given name already exists and logs the actions performed.

    Permissions:
        Only authenticated users can create items.
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Create a new item instance.

        Args:
            request: The request object containing the data to create the item.

        Returns:
            Response: A response object containing the created item or an error message.
        """
        item_name = request.data.get('name')
        if Item.objects.filter(name=item_name).exists():
            logger.error(f'Attempt to create an existing item: {item_name}')
            return Response({'error': 'Item already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        logger.info(f'Creating item: {item_name}')
        return super().create(request, *args, **kwargs)


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete an item.

    This view allows authenticated users to retrieve details of an item, update
    its information, or delete it from the database.

    Permissions:
        Only authenticated users can access item details.
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve an item instance.

        Args:
            request: The request object.
            kwargs: Contains the primary key of the item to retrieve.

        Returns:
            Response: A response object containing the item details or an error message.
        """
        item_id = kwargs.get('pk')
        cache_key = f'item_{item_id}'
        cached_item = cache.get(cache_key)
        if cached_item:
            return Response(cached_item)

        try:
            item = Item.objects.get(pk=item_id)
        except Item.DoesNotExist:
            logger.warning(f'Item not found for ID: {item_id}')
            return Response({'error': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(item)
        cache.set(cache_key, serializer.data)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        Update an existing item instance.

        Args:
            request: The request object containing updated data.
            kwargs: Contains the primary key of the item to update.

        Returns:
            Response: A response object containing the updated item or an error message.
        """
        try:
            return super().update(request, *args, **kwargs)
        except Item.DoesNotExist:
            logger.warning(f'Attempted to update a non-existent item: {kwargs.get("pk")}')
            return Response({'error': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        """
        Delete an item instance.

        Args:
            request: The request object.
            kwargs: Contains the primary key of the item to delete.

        Returns:
            Response: A response object indicating success or an error message.
        """
        try:
            return super().destroy(request, *args, **kwargs)
        except Item.DoesNotExist:
            logger.warning(f'Attempted to delete a non-existent item: {kwargs.get("pk")}')
            return Response({'error': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)
