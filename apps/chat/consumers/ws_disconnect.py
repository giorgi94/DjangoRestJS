@channel_session
def ws_disconnect(message):
    label = message.channel_session['room']
    Group('chat-' + label).discard(message.reply_channel)
