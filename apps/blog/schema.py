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

    def resolve_pk(self, info, **kwargs):
        return self.pk

    def resolve_user(self, info, **kwargs):
        return self.user

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

    user = Field(UserNode)
    blog = Field(BlogNode)

    def resolve_pk(self, info, **kwargs):
        return self.pk

    def resolve_user(self, info, **kwargs):
        return self.user

    def resolve_blog(self, info, **kwargs):
        return self.blog

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
