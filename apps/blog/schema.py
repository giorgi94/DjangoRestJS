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


class BlogQuery:
    blog = relay.Node.Field(BlogNode)
    all_blogs = DjangoFilterConnectionField(BlogNode, blog_pk=Int())

    def resolve_blog_pk(self, info, **kwargs):
        pk = kwargs.get('pk')
        return Blog.objects.filter(pk=pk)

    # def resolve_all_blogs(self, info, **kwargs):
    #     # que
    #     print(kwargs)
    #     return Blog.objects.filter()
