from typing import Union, Tuple

from django.db.models import Model

from snippets import SnippetConst
from snippets.models import Snippet


class SnippetBaseMeta:
    model: Model = Snippet


class _Meta(SnippetBaseMeta):
    fields: Union[str, Tuple[str]] = '__all__'
    read_only_fields: Tuple[str] = (
        SnippetConst.CREATE,
        SnippetConst.UPDATE,
        SnippetConst.HTML,
        SnippetConst.OWNER,
    )
