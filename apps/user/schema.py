from graphene import (
    relay, ObjectType, Schema,
    Int, String, JSONString, List
)
from graphene_django.types import DjangoObjectType
from apps.graphQL.fields import OrderedDjangoFilterConnectionField

from apps.user.models import User


class UserNode(DjangoObjectType):

    pk = Int()

    class Meta:
        model = User
        filter_fields = {
            'id': ['exact'],
            'email': ['exact', 'icontains'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
        }
        interfaces = (relay.Node, )


class UserQuery:
    user = relay.Node.Field(UserNode)
    all_users = OrderedDjangoFilterConnectionField(
        UserNode, pk=Int(), orderBy=List(of_type=String))
