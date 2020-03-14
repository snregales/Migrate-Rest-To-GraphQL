from typing import Union, Tuple

from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from folders import FolderConst
from folders.serializers import FolderBaseMeta
from src import URL


class FolderListSerializer(ModelSerializer):
    owner = StringRelatedField()

    class Meta(FolderBaseMeta):
        fields: Union[str, Tuple[str]] = (
            URL,
            FolderConst.OWNER,
            FolderConst.NAME,)
        read_only_fields: Tuple[str] = fields
