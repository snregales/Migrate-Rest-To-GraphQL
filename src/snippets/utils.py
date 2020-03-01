from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name


def get_highlighted_code(code: str, language: str, style: str, **options) -> str:
    """
    create an html highlighted version of the plain code.

    :param code :type str: code snippet to be highlighted
    :param language :type str: language that the code snippet is written in
    :param style :type str: style to use for highlighting the code
    :return: :type str: highlighted code
    """
    return highlight(
        code=code,
        lexer=get_lexer_by_name(language),
        formatter=HtmlFormatter(style=style, linenos='table', full=True, **options))
