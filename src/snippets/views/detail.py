from typing import Tuple

from django.contrib.auth.models import Permission
from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer

from snippets.models import Snippet
from snippets.serializers.update import SnippetUpdateSerializer
from utils.abstract_views import DetailUpdateViewSet


class SnippetDetailUpdateViewSet(DetailUpdateViewSet):
    queryset: QuerySet = Snippet.objects.all()
    serializer_class: ModelSerializer = SnippetUpdateSerializer
    permission_classes: Tuple[Permission] = (IsAuthenticatedOrReadOnly,)
