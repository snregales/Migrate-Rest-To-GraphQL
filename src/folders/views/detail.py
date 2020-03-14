from typing import Tuple

from django.contrib.auth.models import Permission
from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer

from folders.models import Folder
from folders.serializers.update import FolderUpdateSerializer
from utils.abstract_views import DetailUpdateViewSet


class FolderDetailUpdateViewSet(DetailUpdateViewSet):
    queryset: QuerySet = Folder.objects.all()
    serializer_class: ModelSerializer = FolderUpdateSerializer
    permission_classes: Tuple[Permission] = (IsAuthenticatedOrReadOnly,)
