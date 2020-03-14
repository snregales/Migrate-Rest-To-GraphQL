from django.contrib.auth.base_user import BaseUserManager

from users import UserConst, EMAIL_NOT_SET


class UserManager(BaseUserManager):
    def _create_user(self, email: str, password: str, **extra_fields) -> 'User':
        """Create and save a user with the given email, and password."""
        if not email:
            raise ValueError(EMAIL_NOT_SET)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str = None, **extra_fields) -> 'User':
        extra_fields.setdefault(UserConst.STAFF, False)
        extra_fields.setdefault(UserConst.SUPER, False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields) -> 'User':
        extra_fields.setdefault(UserConst.STAFF, True)
        extra_fields.setdefault(UserConst.SUPER, True)
        extra_fields.setdefault(UserConst.ACTIVE, True)
        return self._create_user(email, password, **extra_fields)
