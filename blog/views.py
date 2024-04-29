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
    json_string = request.body
    telegram_update = json.loads(json_string)
    received_text = telegram_update['message']['text']
    chat_id = telegram_update['message']['chat']['id']
   
    if received_text == '/start':
        # 각 메시지를 별도의 문자열로 정의
        start_message1 = "안녕하세요 개발자 김영희가 만든 VQA 데이터 등록 챗봇입니다."
        start_message2 = "[telegram username 등록]\n\ntelegram의 username을 등록하고 사용해 주세요. \n등록하지 않고 사용 시의 불이익은 본인에게 있습니다.\ntelegram -> settings(설정) -> username(사용자명)"
        start_message3 = "[사용방법]\n\n1. 이미지 업로드\n2. 이미지에 대한 질문 입력\n3. 질문에 대한 답 입력\n\n*최소 7개의 질문과 답을 입력해야 합니다. 사진으로 판단할 수 있는 질문을 입력해야하며, 올바른 답을 입력해주세요.\n\n*질문은 반드시 '?'로 끝나도록 작성하셔야 합니다. 질문 다음에 입력하는 것을 해당 질문에 대한 답입니다.\n\n*챗봇 사용 중 사용방법이 다시 궁금하시다면 '/사용방법'을 입력해주세요."
        start_message4 = "[이미지 전송방법]\n\n이미지는 다음과 같은 방법으로 전송해주세요. \nandroid) 첨부파일->파일->갤러리(압축없이 사진 보내기) \nios) 첨부파일->파일->사진 및 동영상 \nweb) 'send file'을 통해서 이미지 전송"
        start_message5 = "[중지 요청]\n\n중간에 중단하고 싶을 시'/중지'를 입력하세요. \n해당 이미지에 대한 질문과 답은 모두 중단됩니다."

        # 각 메시지를 차례대로 보냄
        bot.sendMessage(chat_id=chat_id, text=start_message1)
        bot.sendMessage(chat_id=chat_id, text=start_message2)
        bot.sendMessage(chat_id=chat_id, text=start_message3)
        bot.sendMessage(chat_id=chat_id, text=start_message4)
        bot.sendMessage(chat_id=chat_id, text=start_message5)

    else:
        text = "ECHO) " + received_text
        bot.sendMessage(chat_id=chat_id, text=text)
    
    return HttpResponse("ok")
