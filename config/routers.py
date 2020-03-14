"""This is the where all routing channels are register for the Migrate-Rest-To-GraphQL project."""

from rest_framework.routers import DefaultRouter

from config import USERS, SNIPPET, FOLDER
from folders.views.detail import FolderDetailUpdateViewSet
from folders.views.list import FolderListCreateViewSet
from snippets.views.detail import SnippetDetailUpdateViewSet
from snippets.views.list import SnippetListCreateViewSet
from users.views.detail import UserDetailUpdateViewSet
from users.views.list import UserListCreateViewSet

router = DefaultRouter()

router.register(USERS, UserListCreateViewSet)
router.register(USERS, UserDetailUpdateViewSet)
router.register(SNIPPET, SnippetListCreateViewSet)
router.register(SNIPPET, SnippetDetailUpdateViewSet)
router.register(FOLDER, FolderListCreateViewSet)
router.register(FOLDER, FolderDetailUpdateViewSet)
