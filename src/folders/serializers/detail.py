from typing import Dict, Any

from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from folders import FolderConst
from folders.models import Folder
from folders.serializers import _Meta
from utils.abstract_serializers import HiddenOwnerMixin


class FolderDetailSerializer(ModelSerializer, HiddenOwnerMixin):
    children = StringRelatedField(many=True)

    def create(self, validated_data: Dict[str, Any]) -> Folder:
        validated_data.setdefault(
            FolderConst.OWNER,
            self.context.get("request").user)
        print(self.context)
        return Folder.objects.create(**validated_data)

    class Meta(_Meta):
        pass
