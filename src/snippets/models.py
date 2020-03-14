from typing import Tuple

from django.db import models

from folders.models import Folder
from misc import user_foreign_key
from snippets import LANGUAGE_CHOICES, STYLE_CHOICES
from snippets.manager import SnippetManager
from utils.abstract_models import TimeStamp, ReprMixin


class Snippet(TimeStamp, ReprMixin):
    """Snippet model"""
    owner = user_foreign_key(related_name='snippets')
    title = models.CharField(max_length=100)
    code = models.TextField()
    html = models.TextField()
    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        default='python',
        max_length=100)
    style = models.CharField(
        choices=STYLE_CHOICES,
        default='friendly',
        max_length=100)
    folder = models.ForeignKey(
        to=Folder,
        on_delete=models.CASCADE,
        related_name='snippets',
        null=True)

    objects: models.Manager = SnippetManager()

    class Meta:
        ordering: Tuple[str] = ('created', 'updated')

    def __str__(self) -> str:
        return self.title
