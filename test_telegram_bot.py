# Polling 방식 => WEB HOOK

import telegram 
from pprint import pprint
from telegram_django_bot import settings


bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)
bot.set_webhook("https://938d-49-167-206-119.ngrok-free.app/blog/webhook/")

# for update in bot.getUpdates():
#     received_text = update.message.text
#     if received_text == "네이버":
#         text = "https://www.naver.com"
#     else:
#         text = "니가 무슨 말 하는 지 모르겠어 ~~~"

#     chat_id = update.message.chat.id # 가장 최근에 온 메세지의 chat id를 가져온다.
#     bot.sendMessage(chat_id=chat_id, text=text)
    
    