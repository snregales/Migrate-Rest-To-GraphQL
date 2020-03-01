from django.db import models

from snippets.utils import get_highlighted_code
from utils.managers import QuerySetManager


class SnippetQuerySet(models.QuerySet):
    def create(self, **kwargs) -> models.Model:
        snippet = super(SnippetQuerySet, self).create(**kwargs)
        snippet.html = get_highlighted_code(
            code=snippet.code,
            language=snippet.language,
            style=snippet.style,
            title=snippet.title)
        snippet.save()
        return snippet


class SnippetManager(QuerySetManager):
    def get_queryset(self) -> models.QuerySet:
        """
        Overridden parent method.

        :return :type QuerySet
        """
        return SnippetQuerySet(self.model, using=self._db)
