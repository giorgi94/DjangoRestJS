from graphene import (
    relay, ObjectType, Schema,
    Int, String, JSONString, List
)
from graphene_django.types import DjangoObjectType
from apps.graphQL.fields import DjangoConnectionField

from apps.user.models import User


class UserNode(DjangoObjectType):

    pk = Int()

    class Meta:
        model = User
        filter_fields = []
        interfaces = (relay.Node, )


class UserQuery:
    user = relay.Node.Field(UserNode)
    all_users = DjangoConnectionField(UserNode)
