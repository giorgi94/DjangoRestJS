from graphene import ObjectType, Schema
from apps.blog.schema import BlogQuery
from apps.user.schema import UserQuery


class Query(UserQuery, BlogQuery, ObjectType):
    pass


schema = Schema(query=Query)

"""
json.dumps(schema.execute('''
{
  allBlogs {
    edges {
      node {
        pk
        alias
        title
        pubDate
        isPub
      }
      cursor
    }
    pageInfo {
      startCursor
      endCursor
      hasNextPage
      hasPreviousPage
    }
  }
}
''').data, ensure_ascii=False)
"""
