from django.db import models

from folders import FolderConst
from utils.managers import QuerySetManager


class FolderQuerySet(models.QuerySet):
    def create(self, **kwargs) -> models.Model:
        folder = super(FolderQuerySet, self).create(**kwargs)
        folder.parent = kwargs.get(FolderConst.PARENT)
        folder.save()
        return folder


class FolderManager(QuerySetManager):
    def get_queryset(self) -> models.QuerySet:
        """
        Overridden parent method.

        :return :type QuerySet
        """
        return FolderQuerySet(self.model, using=self._db)

    def create_home(self, owner: models.Model):
        return self.get_queryset().create(
            owner=owner,
            name='~',)
