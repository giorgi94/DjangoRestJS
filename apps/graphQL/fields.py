from graphene import (
    Int, String, List
)
from copy import copy
from functools import partial
from graphene.types.argument import to_arguments
from graphene.types.generic import GenericScalar
from graphene_django.fields import DjangoConnectionField as BaseDjangoConnectionField


class DjangoFilterConnectionField(BaseDjangoConnectionField):

    def __init__(self, type, fields=None, order_by=None,
                 extra_filter_meta=None, filterset_class=None,
                 *args, **kwargs):
        self._fields = fields
        self._provided_filterset_class = filterset_class
        self._filterset_class = None
        self._extra_filter_meta = extra_filter_meta
        self._base_args = None
        self.filtering_args = None
        self.filterset_class = None
        super().__init__(type, *args, **kwargs)

    @property
    def args(self):
        return to_arguments(self._base_args or OrderedDict(), self.filtering_args)

    @args.setter
    def args(self, args):
        self._base_args = args

    @classmethod
    def connection_resolver(cls, resolver, connection, default_manager, max_limit,
                            enforce_first_or_last, filterset_class, filtering_args,
                            root, info, **args):

        qs = default_manager.get_queryset()

        return super(DjangoFilterConnectionField, cls).connection_resolver(
            resolver,
            connection,
            qs,
            max_limit,
            enforce_first_or_last,
            root,
            info,
            **args
        )

    def get_resolver(self, parent_resolver):
        return partial(
            self.connection_resolver,
            parent_resolver,
            self.type,
            self.get_manager(),
            self.max_limit,
            self.enforce_first_or_last,
            self.filterset_class,
            self.filtering_args
        )


class DjangoConnectionField(DjangoFilterConnectionField):

    def __init__(self, *args, **kwargs):

        kwargs.update({
            'pk': Int(),
            'orderBy': List(of_type=String),
            'filterBy': GenericScalar(),
        })

        super().__init__(*args, **kwargs)

    @classmethod
    def connection_resolver(cls, resolver, connection, default_manager, max_limit,
                            enforce_first_or_last, filterset_class, filtering_args,
                            root, info, **kwargs):

        filterBy = kwargs.get('filterBy', {})
        qs = default_manager.get_queryset().filter(**filterBy)

        model = default_manager.model

        if 'default_Q' in model.__dict__:
            qs = qs.filter(model.default_Q())

        orderBy = kwargs.get('orderBy', None)

        if orderBy:
            qs = qs.order_by(*orderBy)
        return super(DjangoFilterConnectionField, cls).connection_resolver(
            resolver,
            connection,
            qs,
            max_limit,
            enforce_first_or_last,
            root,
            info,
            **kwargs
        )
