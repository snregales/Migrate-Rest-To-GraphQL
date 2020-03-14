from rest_framework.fields import CurrentUserDefault, HiddenField


class HiddenOwnerMixin:
    owner = HiddenField(default=CurrentUserDefault)
