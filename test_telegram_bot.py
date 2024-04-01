# Polling 방식

import telegram 
from pprint import pprint

my_token = "6983964934:AAFD4D7FCtRfV5jNEn_n_ZRq6uz-_DVFXj4" 

bot = telegram.Bot(token = my_token)

for update in bot.getUpdates():
    received_text = update.message.text
    if received_text == "네이버":
        text = "https://www.naver.com"
    else:
        text = "니가 무슨 말 하는 지 모르겠어 ~~~"

    chat_id = update.message.chat.id # 가장 최근에 온 메세지의 chat id를 가져온다.
    bot.sendMessage(chat_id=chat_id, text=text)
    
