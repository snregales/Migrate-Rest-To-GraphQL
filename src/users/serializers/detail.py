from typing import Any, Dict

from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from users.serializers import _Meta

User = get_user_model()


class UserDetailSerializer(ModelSerializer):
    def create(self, validated_data: Dict[str, Any]) -> User:
        return User.objects.create_user(**validated_data)

    class Meta(_Meta):
        pass
