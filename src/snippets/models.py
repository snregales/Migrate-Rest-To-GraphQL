from typing import List

from django.db import models

from snippets import LANGUAGE_CHOICES, STYLE_CHOICES
from snippets.manager import SnippetManager
from utils.abstract_models import TimeStamp


class Snippet(TimeStamp):
    """Snippet model"""
    owner = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='snippets')
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

    objects: models.Manager = SnippetManager()

    class Meta:
        ordering: List[str] = ['created', 'updated']

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}({self.__str__()!r})>'
