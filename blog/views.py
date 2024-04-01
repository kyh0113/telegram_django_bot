import json
import telegram
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render

bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)

def index(request):
    return HttpResponse('Hello Django')

@csrf_exempt
def webhook(request):
    print()
    print(request)
    json_string = request.body
    telegram_update = json.loads(json_string)
    print("dkdkdkdk")

    received_text = telegram_update['message']['text']
    print(received_text)

    text = "ECHO) " + received_text
    chat_id = telegram_update['message']['chat']['id']
    bot.sendMessage(chat_id = chat_id, text = text)
    return HttpResponse("ok")
