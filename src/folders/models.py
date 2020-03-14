from typing import Tuple

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from folders.manager import FolderManager
from misc import user_foreign_key
from utils.abstract_models import ReprMixin, TimeStamp


class Folder(TimeStamp, ReprMixin):
    """Folder model."""
    owner = user_foreign_key(related_name='folders')
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,)

    objects = FolderManager()

    class Meta:
        ordering: Tuple[str] = ('created', 'updated')
        unique_together: Tuple[str] = ('owner', 'name', 'parent')

    def __str__(self) -> str:
        return self.name


User: models.Model = get_user_model()


@receiver(post_save, sender=User)
def create_home_folder(instance: User, created: bool, *args, **kwargs):
    if created and not instance.is_superuser:
        Folder.objects.create_home(owner=instance)
