import sys

from rest_framework.generics import ListCreateAPIView, GenericAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ViewSetMixin


class ListDetailSerializerMixin(GenericAPIView):
    list_serializer_class: ModelSerializer = None

    def get_serializer(self, *args, **kwargs) -> ModelSerializer:
        """
        Override parents get_serializer method.

        In order to return a different, list, serializer,
        if the thread being call is list
        otherwise continue normally as expected

        :return :type ModelSerializer; List or Detail
        """
        # if method is not called by a list thread return parents serializer_class
        if sys._getframe().f_back.f_code.co_name != 'list':
            return super(ListDetailSerializerMixin, self).get_serializer(*args, **kwargs)
        # reassign serializer_class to be the list serializer class
        serializer_class = self.get_list_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_list_serializer_class(self) -> ModelSerializer:
        assert self.list_serializer_class is not None, (
            f"""'{self.__class__.__name__}' should either include a `serializer_class` attribute, 
or override the `get_serializer_class()` method."""
        )
        return self.list_serializer_class


class ListCreateViewSet(ViewSetMixin,
                        ListCreateAPIView,
                        ListDetailSerializerMixin):
    class Meta:
        abstract: bool = True


class DetailViewSet(ViewSetMixin, RetrieveAPIView):
    class Meta:
        abstract: bool = True


class DetailUpdateViewSet(DetailViewSet, UpdateAPIView):
    class Meta:
        abstract: bool = True
