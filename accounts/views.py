import logging

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import UserRegistrationSerializer

logger = logging.getLogger(__name__)


class UserRegisterView(generics.CreateAPIView):
    """
    API View for user registration.

    This view handles the registration of a new user and returns the user's data
    along with a JWT token upon successful registration.
    """

    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Handle the POST request for user registration.

        Args:
            request (Request): The incoming request with user data.

        Returns:
            Response: A JSON response containing the user data or error messages.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            logger.info(f"User registered successfully: {user.username}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning(f"User registration failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
