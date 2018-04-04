# from . import consumers
#
# channel_routing = {
#     'websocket.connect': consumers.ws_connect,
#     'websocket.receive': consumers.ws_receive,
#     'websocket.disconnect': consumers.ws_disconnect,
# }

# channel_routing = {}

from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
})
