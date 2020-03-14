from typing import Any, Dict

from rest_framework.serializers import ModelSerializer

from folders.models import Folder
from misc import NOT_REQUIRED
from snippets import SnippetConst
from snippets.serializers import _Meta


class SnippetUpdateSerializer(ModelSerializer):

    class Meta(_Meta):
        extra_kwargs: Dict[str, Any] = {
            SnippetConst.LANG: NOT_REQUIRED,
            SnippetConst.TITLE: NOT_REQUIRED,
            SnippetConst.CODE: NOT_REQUIRED,
            SnippetConst.STYLE: NOT_REQUIRED,
        }
