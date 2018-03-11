from graphene import (
    relay, ObjectType, Schema,
    Int, String, JSONString
)
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from apps.blog.models import Blog


class BlogNode(DjangoObjectType):

    pk = Int()

    def resolve_pk(self, info, **kwargs):
        return self.pk

    class Meta:
        model = Blog
        filter_fields = {
            'id': ['exact'],
            'title': ['exact', 'icontains'],
            'content': ['exact', 'icontains'],
            'abstract': ['exact', 'icontains'],
            'abstract': ['exact', 'icontains'],
        }
        interfaces = (relay.Node, )



# class OrderedDjangoFilterConnectionField(DjangoFilterConnectionField):
#     @classmethod
#     def connection_resolver(cls, resolver, connection, default_manager, max_limit,
#                             enforce_first_or_last, filterset_class, filtering_args,
#                             root, info, **args):

    
#         filter_kwargs = {k: v for k, v in args.items() if k in filtering_args}
#         qs = default_manager.get_queryset()
#         qs = filterset_class(data=filter_kwargs, queryset=qs).qs
#         order = args.get('orderBy', None)
#         if order:
#             qs = qs.order_by(*order)

#         return super(DjangoFilterConnectionField, cls).connection_resolver(
#             resolver,
#             connection,
#             qs,
#             max_limit,
#             enforce_first_or_last,
#             root,
#             info,
#             **args
#         )


class BlogQuery:
    blog = relay.Node.Field(BlogNode)
    all_blogs = DjangoFilterConnectionField(BlogNode, pk=Int())

    # def resolve_all_blogs(self, info, **kwargs):
    #     kw = kwargs.copy()
    #     if()
    #     return Blog.objects.filter(**kw)


'''
import base64
#id
base64.urlsafe_b64encode('BlogNode:2'.encode()).decode()
base64.urlsafe_b64decode('QmxvZ05vZGU6Mg==').decode() 

#endCursor
first: 2
'arrayconnection:1'
'arrayconnection:3'
'arrayconnection:5'

first: 5
'arrayconnection:4'
'arrayconnection:9'
'arrayconnection:14'

'''