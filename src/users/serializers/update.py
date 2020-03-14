from typing import Tuple, Any, Dict

from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from misc import NOT_REQUIRED
from users import UserConst
from utils.abstract_models import UserBaseMeta

User = get_user_model()


class UserUpdateSerializer(ModelSerializer):
    class Meta(UserBaseMeta):
        fields: Tuple[str] = (
            UserConst.F_NAME, UserConst.L_NAME,
            UserConst.EMAIL)
        read_only_fields: Tuple[str] = (UserConst.EMAIL,)
        extra_kwargs: Dict[str, Any] = {
            UserConst.F_NAME: NOT_REQUIRED,
            UserConst.L_NAME: NOT_REQUIRED,
        }
