from django.conf.global_settings import AUTH_USER_MODEL

from folders.apps import FolderConfig
from snippets.apps import SnippetConfig

# Django Rest Framework
REST: str = 'rest_framework'
REST_PAGE: str = f'{REST}.pagination'

# url
REST_URL: str = f'{REST}.urls'

# Route names
USERS: str = 'users'
SNIPPET: str = SnippetConfig.name
FOLDER: str = FolderConfig.name
