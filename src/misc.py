from functools import partial
from typing import Any, Dict

from django.db import models

REQUIRED: str = 'required'
NOT_REQUIRED: Dict[str, Any] = {REQUIRED: False}

user_foreign_key = partial(
    models.ForeignKey,
    to='users.User',  # get_user_model will not work, users.User is not yet loaded
    on_delete=models.CASCADE,
)
