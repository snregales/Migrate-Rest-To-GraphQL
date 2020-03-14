from typing import Tuple, Union

from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from snippets import SnippetConst
from snippets.serializers import SnippetBaseMeta
from src import URL


class SnippetListSerializer(ModelSerializer):
    owner = StringRelatedField()

    class Meta(SnippetBaseMeta):
        fields: Union[str, Tuple[str]] = (
            URL,
            SnippetConst.OWNER,
            SnippetConst.TITLE,
            SnippetConst.LANG,)
        read_only_fields: Tuple[str] = fields
