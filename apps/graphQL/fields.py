from graphene_django.filter import DjangoFilterConnectionField
from graphene import (
    Int, String, List
)
from graphene.types.generic import GenericScalar


class DjangoConnectionField(DjangoFilterConnectionField):

    def __init__(self, *args, **kwargs):

        kwargs.update({
            'pk': Int(),
            'orderBy': List(of_type=String),
            'filterBy': GenericScalar()
        })

        super().__init__(*args, **kwargs)

    @classmethod
    def connection_resolver(cls, resolver, connection, default_manager, max_limit,
                            enforce_first_or_last, filterset_class, filtering_args,
                            root, info, **args):

        filter_kwargs = {k: v for k, v in args.items() if k in filtering_args}
        filterBy = args.get('filterBy', {})

        qs = filterset_class(
            data=filter_kwargs,
            queryset=default_manager.get_queryset().filter(**filterBy),
            request=info.context
        ).qs

        orderBy = args.get('orderBy', None)

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
            **args
        )
