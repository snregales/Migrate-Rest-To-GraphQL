from django.contrib.auth import get_user_model
from django.db import models


class ReprMixin:
    def __str__(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}({self.__str__()!r})>'


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract: bool = True


class UserBaseMeta:
    model = get_user_model()
