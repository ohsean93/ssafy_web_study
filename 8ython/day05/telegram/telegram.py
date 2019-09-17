from flask import Flask
import random
import requests
import bs4
from decouple import config

base_url = "https://api.telegram.org/"
sendMessage = 'sendMessage'
chat_id = config('CHAT_ID')
text = "hi"
bot_token = config('TELEGRAM_TOKEN')


url = f"{base_url}/bot{bot_token}/{sendMessage}?chat_id={chat_id}&text={text}"

res = requests.get(url)

print(res)
print(res.text)