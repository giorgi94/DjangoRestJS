from graphene import (
    relay, ObjectType, Schema,
    Int, String, JSONString, List, Field
)
from graphene_django.types import DjangoObjectType
from apps.graphQL.fields import DjangoConnectionField

from apps.blog.models import Blog, Comment, Category, Tag
from apps.user.schema import UserNode


class TagNode(DjangoObjectType):
    pk = Int()

    class Meta:
        model = Tag
        interfaces = (relay.Node, )


class CategoryNode(DjangoObjectType):
    pk = Int()

    class Meta:
        model = Category
        interfaces = (relay.Node, )


class BlogNode(DjangoObjectType):
    pk = Int()

    class Meta:
        model = Blog
        interfaces = (relay.Node, )

class CommentNode(DjangoObjectType):
    pk = Int()

    class Meta:
        model = Comment
        interfaces = (relay.Node, )


class BlogQuery:
    blog = relay.Node.Field(BlogNode)
    all_blogs = DjangoConnectionField(BlogNode)

    comment = relay.Node.Field(CommentNode)
    all_comments = DjangoConnectionField(CommentNode)

    tag = relay.Node.Field(TagNode)
    all_tags = DjangoConnectionField(TagNode)
