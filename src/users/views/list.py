from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from rest_framework.serializers import ModelSerializer

from users.serializers.detail import UserDetailSerializer
from users.serializers.list import UserListSerializer
from utils.abstract_views import ListCreateViewSet

User = get_user_model()


class UserListCreateViewSet(ListCreateViewSet):
    queryset: QuerySet = User.objects.all()
    serializer_class: ModelSerializer = UserDetailSerializer
    list_serializer_class: ModelSerializer = UserListSerializer
