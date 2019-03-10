from django.shortcuts import render
from django.http import JsonResponse
from app.models import Menu
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.views.decorators.csrf import csrf_exempt
import json, datetime
# Create your views here.

def keyboard(request):

    return JsonResponse({
        'type': 'buttons',
        'buttons': ['아침', '점심', '저녁']
    })


@csrf_exempt
def message(request):
    
    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)
    content_name = received_json['content']
    today = datetime.date.today()
    today_date = today.strftime("%m월 %d일")
    today_weekday = today.weekday()

    if content_name == '아침':
        try:
             with open('~/json/haksik.json', 'r') as f:
                datas = json.load(f)
             if today_weekday == 0:
                 meal = str(datas.get('mon'))
                            
               

             return JsonResponse({
 
                'message' : {
                'text':today_date + '의 ' +  content_name + '메뉴 입니다. \n ' + meal 
                     },

                'keyboard' : {
                    'type': 'buttons',
                    'buttons': ['아침', '점심', '저녁']
                    }
                })
        finally:
            f.close() 
