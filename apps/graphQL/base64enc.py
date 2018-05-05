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


def page_to_cursor(per_page, page):
    try:
        if page == 1:
            return {
                'first': per_page,
                'after': ""
            }

        pg = (page - 1) * per_page - 1

        return {
            'first': per_page,
            'after': encode('arrayconnection:%d' % pg)
        }
    except:
        return None


'''
##JS
btoa('BlogNode:23') = "QmxvZ05vZGU6MjM="
atob('QmxvZ05vZGU6MjM=') = "BlogNode:23"

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
first:per_page, after: ""
page: 2
first:per_page, after: arrayconnection:per_page-1

'''
