import os
import channels.layers

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoexample.settings")
channel_layer = channels.layers.get_channel_layer()
