from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from .models import InventoryItem
from .serializers import InventoryItemSerializer
import logging

logger = logging.getLogger(__name__)


class ItemCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = InventoryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Item created: {serializer.data['name']}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Item creation failed")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, item_id):
        item = cache.get(f"item_{item_id}")
        if not item:
            try:
                item = InventoryItem.objects.get(pk=item_id)
                serializer = InventoryItemSerializer(item)
                cache.set(f"item_{item_id}", serializer.data)
                logger.info(f"Item retrieved from DB: {item_id}")
            except InventoryItem.DoesNotExist:
                logger.error(f"Item not found: {item_id}")
                return Response({"detail": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            logger.info(f"Item retrieved from cache: {item_id}")
        return Response(item)

    def put(self, request, item_id):
        try:
            item = InventoryItem.objects.get(pk=item_id)
        except InventoryItem.DoesNotExist:
            return Response({"detail": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = InventoryItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete(f"item_{item_id}")
            logger.info(f"Item updated: {item_id}")
            return Response(serializer.data)
        logger.error("Item update failed")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id):
        try:
            item = InventoryItem.objects.get(pk=item_id)
            item.delete()
            cache.delete(f"item_{item_id}")
            logger.info(f"Item deleted: {item_id}")
            return Response({"detail": "Item deleted"}, status=status.HTTP_204_NO_CONTENT)
        except InventoryItem.DoesNotExist:
            logger.error(f"Item not found: {item_id}")
            return Response({"detail": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
