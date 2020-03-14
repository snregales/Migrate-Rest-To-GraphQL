from typing import Tuple

from django.contrib.auth.models import Permission
from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer

from folders.models import Folder
from folders.serializers.detail import FolderDetailSerializer
from folders.serializers.list import FolderListSerializer
from utils.abstract_views import ListCreateViewSet


class FolderListCreateViewSet(ListCreateViewSet):
    permission_classes: Tuple[Permission] = (IsAuthenticatedOrReadOnly,)
    queryset: QuerySet = Folder.objects.all()
    serializer_class: ModelSerializer = FolderDetailSerializer
    list_serializer_class: ModelSerializer = FolderListSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and not (user.is_superuser or user.is_staff):
            self.queryset = Folder.objects.filter(owner=self.request.user)
        return super(FolderListCreateViewSet, self).get_queryset()
