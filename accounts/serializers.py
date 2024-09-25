import logging
from django.contrib.auth.models import User
from rest_framework import serializers

# Configure logging
logger = logging.getLogger(__name__)


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.

    This serializer handles the creation of a new user instance, including validation of
    the provided username, email, and password.
    """

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create a new user with the validated data.

        Args:
            validated_data (dict): Validated data for user creation.

        Returns:
            User: The created user instance.
        """
        try:
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password']
            )
            logger.info(f"User created successfully: {user.username}")
            return user
        except Exception as e:
            logger.error(f"Error creating user: {e}")
            raise serializers.ValidationError("User registration failed.")
