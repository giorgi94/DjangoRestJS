import graphene
from graphene_django.types import DjangoObjectType

from apps.blog.models import Blog


class BlogObjectType(DjangoObjectType):

    class Meta:
        model = Blog


class QueryType(graphene.ObjectType):
    name = "Query"
    description = "..."

    blogs = graphene.List(BlogObjectType)

    def resolve_blogs(self, info, **kwargs):
        return Blog.active_blogs()


schema = graphene.Schema(
    query=QueryType
)
