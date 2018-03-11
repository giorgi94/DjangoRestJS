from graphene import (
    relay, ObjectType, Schema,
    Int, String, JSONString, List
)
from graphene_django.types import DjangoObjectType
from apps.graphQL.fields import OrderedDjangoFilterConnectionField

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


class BlogQuery:
    blog = relay.Node.Field(BlogNode)
    all_blogs = OrderedDjangoFilterConnectionField(
        BlogNode, pk=Int(), orderBy=List(of_type=String))
