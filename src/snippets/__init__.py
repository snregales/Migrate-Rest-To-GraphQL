from typing import List, Tuple

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from utils import TimeStampConst

LEXER_ALIASES = 1
LEXER_NAME = 0
# for all lexers that have aliases, retrieve its alias and name in sorted order
LANGUAGE_CHOICES: List[Tuple[str, str]] = sorted(
    map(
        lambda lexer: (lexer[LEXER_ALIASES][0], lexer[LEXER_NAME]) if lexer[LEXER_ALIASES] else None,
        get_all_lexers()))
STYLE_CHOICES: List[Tuple[str, str]] = sorted(map(lambda style: (style, style), get_all_styles()))


class SnippetConst(TimeStampConst):
    OWNER: str = 'owner'
    TITLE: str = 'title'
    CODE: str = 'code'
    HTML: str = 'html'
    LANG: str = 'language'
    STYLE: str = 'style'
