from typing import Union, Tuple, Dict, Any

from rest_framework.serializers import ModelSerializer

from folders import FolderConst
from folders.models import Folder
from folders.serializers import _Meta
from folders.serializers.detail import FolderDetailSerializer
from folders.utils import add_child_folder
from misc import NOT_REQUIRED


class FolderUpdateSerializer(ModelSerializer):
    children = FolderDetailSerializer(many=True)

    def update(self, instance: Folder, validated_data: Dict[str, Any]) -> Folder:
        add_child_folder(
            instance=instance,
            user=self.context.get('request').user,
            **validated_data.pop(FolderConst.CHILD, None))
        return instance

    class Meta(_Meta):
        fields: Union[Tuple[str]] = (
            FolderConst.NAME,
            FolderConst.CHILD,
            FolderConst.CREATE,
            FolderConst.UPDATE,
            FolderConst.OWNER,
            FolderConst.PARENT,
        )
        read_only_fields: Tuple[str] = fields[2:]
        extra_kwargs: Dict[str, Any] = {
            FolderConst.NAME: NOT_REQUIRED,
            FolderConst.CHILD: NOT_REQUIRED,
        }
