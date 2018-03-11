import base64


def encode(e):
    # BlogNode:2 -> QmxvZ05vZGU6Mg==
    try:
        return base64.urlsafe_b64encode(e.encode()).decode()
    except:
        return None


def decode(e):
    # QmxvZ05vZGU6Mg== -> BlogNode:2
    try:
        return base64.urlsafe_b64decode(e).decode()
    except:
        return None


def cursor_page(page, per_page):
    first = per_page
    after = encode('arrayconnection:' + str(page * first - 1))
    return (first, after)


'''
import base64
#id
base64.urlsafe_b64encode('BlogNode:2'.encode()).decode()
base64.urlsafe_b64decode('QmxvZ05vZGU6Mg==').decode()

#endCursor
first: 2
'arrayconnection:1'
'arrayconnection:3'
'arrayconnection:5'

first: 5
'arrayconnection:4'
'arrayconnection:9'
'arrayconnection:14'


per_page: 20
page: 1
first:per_page, after: arrayconnection:per_page-1
page: 2
first:per_page, after: arrayconnection:2per_page-1

'''
