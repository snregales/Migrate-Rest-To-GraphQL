from typing import Tuple, Union

from django.db.models import Model

from folders import FolderConst
from folders.models import Folder


class FolderBaseMeta:
    model: Model = Folder


class _Meta(FolderBaseMeta):
    fields: Union[str, Tuple[str]] = '__all__'
    read_only_fields: Tuple[str] = (
        FolderConst.CREATE,
        FolderConst.UPDATE,
        FolderConst.OWNER,
        FolderConst.PARENT,
    )
