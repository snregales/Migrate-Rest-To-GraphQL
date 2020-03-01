from django.db import models


class QuerySetManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        raise NotImplementedError


class InnerClassQuerySetManager(QuerySetManager):
    """A re-usable Manager to access a custom QuerySet"""

    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            # don't delegate internal methods to the queryset
            if attr.startswith('__') and attr.endswith('__'):
                raise
            return getattr(self.get_query_set(), attr, *args)

    def get_queryset(self) -> models.QuerySet:
        return self.model.QuerySet(self.model, using=self._db)
