from graphene import (
    relay, ObjectType, Schema,
    Int, String, JSONString, List, Field
)
from graphene_django.types import DjangoObjectType
from apps.graphQL.fields import OrderedDjangoFilterConnectionField

from apps.blog.models import Blog, Comment
from apps.user.schema import UserNode


class BlogNode(DjangoObjectType):

    pk = Int()
    user = Field(UserNode)

    class Meta:
        model = Blog
        filter_fields = {
            'title': ['exact', 'icontains'],
            'content': ['exact', 'icontains'],
            'abstract': ['exact', 'icontains'],
        }
        interfaces = (relay.Node, )


class BlogQuery:
    blog = relay.Node.Field(BlogNode)
    all_blogs = OrderedDjangoFilterConnectionField(
        BlogNode, pk=Int(), orderBy=List(of_type=String))


class CommentNode(DjangoObjectType):
    
    pk = Int()
    user = Field(UserNode)
    blog = Field(BlogNode)

    class Meta:
        model = Comment
        filter_fields = {
            'content': ['exact', 'icontains'],
        }
        interfaces = (relay.Node, )


class CommentQuery:
    comment = relay.Node.Field(CommentNode)
    all_comments = OrderedDjangoFilterConnectionField(
        CommentNode, orderBy=List(of_type=String))
