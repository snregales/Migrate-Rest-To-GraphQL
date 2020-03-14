from django.db.models import QuerySet
from rest_framework.serializers import ModelSerializer

from utils.abstract_views import DetailUpdateViewSet

from . import User
from ..serializers.update import UserUpdateSerializer


class UserDetailUpdateViewSet(DetailUpdateViewSet):
    queryset: QuerySet = User.objects.all()
    serializer_class: ModelSerializer = UserUpdateSerializer
