from typing import Tuple, Dict, Any

from users import UserConst
from utils.abstract_models import UserBaseMeta


class _Meta(UserBaseMeta):
    fields: Tuple[str] = (
        UserConst.F_NAME, UserConst.L_NAME,
        UserConst.EMAIL, UserConst.PASS,)
    extra_kwargs: Dict[str, Any] = {
        UserConst.PASS: {'write_only': True}
    }
