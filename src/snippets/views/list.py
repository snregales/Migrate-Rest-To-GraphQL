from typing import Tuple

from django.contrib.auth.models import Permission
from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer

from snippets.models import Snippet
from snippets.serializers.detail import SnippetDetailSerializer
from snippets.serializers.list import SnippetListSerializer
from utils.abstract_views import ListCreateViewSet


class SnippetListCreateViewSet(ListCreateViewSet):
    permission_classes: Tuple[Permission] = (IsAuthenticatedOrReadOnly,)
    queryset: QuerySet = Snippet.objects.all()
    serializer_class: ModelSerializer = SnippetDetailSerializer
    list_serializer_class: ModelSerializer = SnippetListSerializer
