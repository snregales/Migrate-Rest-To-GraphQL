from typing import Any, Dict

from rest_framework.fields import CurrentUserDefault, HiddenField
from rest_framework.serializers import ModelSerializer

from snippets.models import Snippet
from snippets.serializers import _Meta
from utils.abstract_serializers import HiddenOwnerMixin


class SnippetDetailSerializer(ModelSerializer, HiddenOwnerMixin):
    def create(self, validated_data: Dict[str, Any]) -> Snippet:
        return Snippet.objects.create(**validated_data)

    class Meta(_Meta):
        pass
