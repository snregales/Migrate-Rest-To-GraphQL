from typing import Tuple

from rest_framework.serializers import ModelSerializer

from src import URL
from users import UserConst
from users.serializers import _Meta


class UserListSerializer(ModelSerializer):
    class Meta(_Meta):
        fields: Tuple[str] = (URL, UserConst.FULL, UserConst.EMAIL)
        read_only_fields: Tuple[str] = fields
