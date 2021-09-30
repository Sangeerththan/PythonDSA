import configparser
import json
import re
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
PeerChannel
)

api_id = '*******'
api_hash = '**************************'
client = TelegramClient('anon', api_id, api_hash)

user_input_channel = 'https://t.me/ReutersWorldChannel'

@client.on(events.NewMessage(chats=user_input_channel))
async def newMessageListener(event):
    newMessage = event.message.message
    print(newMessage)

with client:
    client.run_until_disconnected()