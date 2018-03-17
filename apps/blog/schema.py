from graphene import (
    relay, ObjectType, Schema,
    Int, String, JSONString, List, Field
)
from graphene_django.types import DjangoObjectType
from apps.graphQL.fields import DjangoConnectionField

from apps.blog.models import Blog, Comment
from apps.user.schema import UserNode


class BlogNode(DjangoObjectType):

    pk = Int()
    user = Field(UserNode)

    class Meta:
        model = Blog
        filter_fields = []
        interfaces = (relay.Node, )


class BlogQuery:
    blog = relay.Node.Field(BlogNode)
    all_blogs = DjangoConnectionField(BlogNode)


class CommentNode(DjangoObjectType):

    pk = Int()
    user = Field(UserNode)
    blog = Field(BlogNode)

    class Meta:
        model = Comment
        filter_fields = []
        interfaces = (relay.Node, )


class CommentQuery:
    comment = relay.Node.Field(CommentNode)
    all_comments = DjangoConnectionField(CommentNode)
