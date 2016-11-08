
# subscribe to your PubNub channel using this code
# SwitchDoc Labs November, 2016
from pubnub import Pubnub

# configuration
Pubnub_Publish_Key = "pub-c-xxxxx"
Pubnub_Subscribe_Key = "sub-c-xxxx"


pubnub = Pubnub(publish_key=Pubnub_Publish_Key, subscribe_key=Pubnub_Subscribe_Key)
channel = "SunIOT_Sunlight"

def callback(message, channel):
    print('[' + channel + ']: ' + str(message))

pubnub.subscribe(
    channel,
    callback = callback)

