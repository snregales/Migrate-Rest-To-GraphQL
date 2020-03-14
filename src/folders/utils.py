from django.contrib.auth import get_user_model

from folders.models import Folder


def add_child_folder(instance: Folder, user: get_user_model,  **kwargs) -> None:
    if kwargs:
        instance.children.add(Folder(owner=user, **kwargs), bulk=False)
        instance.save()
