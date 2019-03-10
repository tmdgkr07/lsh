from django.shortcuts import render
from django.http import JsonResponse
from app.models import Menu
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.views.decorators.csrf import csrf_exempt
import json,datetime
from datetime import timedelta
from dateutil.relativedelta import *
# Create your views here.

def keyboard(request):

    return JsonResponse({
        'type': 'buttons',
        'buttons': ['오늘의 학식', '패 치 중','처음으로']
    })


@csrf_exempt
def message(request):
    


    days = ['mon','tue','wed','thu','fri','sat','sun']
    day_tomorrow = ['tue','wed','thu','fri','sat','sun','mon']
    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)
    content_name = received_json['content']
    today = datetime.date.today()
    today_date = today.strftime("%m월 %d일")
    today_weekday = today.weekday()
    tomorrow = today+timedelta(days=1)
    tomorrow_date = tomorrow.strftime("%m월 %d일")                
    
    if content_name == '오늘의 학식':
        return JsonResponse({
            'message':{
                'text':'※ 원하는 시간대를 눌러주세요'
                },
            'keyboard':{
                'type': 'buttons',
             'buttons': ['아침', '점심', '저녁','처음으로']
             }
            })        
    if content_name =='아침':        
            return JsonResponse({
         
                'message' : {
                'text':today_date + '의 ' +  content_name + '메뉴 입니다. \n ' + Menu.objects.get(day=days[today_weekday], time=content_name).menu
                     },

                'keyboard' : {
                    'type': 'buttons',
                    'buttons': ['아침', '점심', '저녁','처음으로']
                             }
                }) 
    if content_name =='점심':
            return JsonResponse({

                 'message': {
                    'text':today_date + '의' + content_name + '메뉴 입니다. \n '  + Menu.objects.get(day=days[today_weekday], time=content_name).menu
                     },

                'keyboard' : { 
                 'type': 'buttons',
                 'buttons': ['아침', '점심', '저녁','처음으로']
                 }
                })
    if content_name =='저녁':
                return JsonResponse({               
                    'message':{ 
                    'text':today_date + '의' + content_name + '메뉴 입니다. \n '  + Menu.objects.get(day=days[today_weekday], time=content_name).menu
                    },
                    'keyboard' : {
                        'type' : 'buttons',
                     'buttons' : ['아침', '점심', '저녁','처음으로'] 
                     }
                                                                                                                                                                                                                                                                  })

    if content_name == '처음으로':
            return JsonResponse({
                 'message' : {
                    'text' : '※ 처음으로 돌아갑니다'
                    },
                 'keyboard' : {
                     'type' : 'buttons',
                  'buttons' : ['오늘의 학식', '패 치 중','처음으로']
                   }
                 })

    if content_name == '패 치 중':
                return JsonResponse({
                    'message' : { 
                        'text': '※ 새로운 기능을 위해 패치를 진행중입니다. 기대해주세요 ~~'
                },
                     
                'keyboard' : {
                'type' : 'buttons',
                'buttons' : ['오늘의 학식', '패 치 중','처음으로']

                } })                                                          

#    if content_name == '점심':
#        return JsonResponse({
#            'message' : {
#                'text': today_date + '의 ' + content_name + '메뉴 입니다. \n ' + Menu.objects.get(day=days[today_weekday], time='중식').menu
#               },
#            'keyboard': {
#                'type': 'buttons',
#                'buttons': ['아침', '점심', '저녁']
#                }                
#
#                }) 
             
#def json_response(message_text):
#
#    return JsonResponse({
#        'keyboard': {
#            'type': 'buttons',
#         'buttons': ['아침', '점심', '저녁']
#            }
#        })

def crawl(request):
    flush_menu_db()
    today = 0
    day = [ 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    day_tomorrow = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    html =urlopen('http://www.kopo.ac.kr/gwangju/content.do?menu=4636')
    source= html.read().decode('utf-8')
    html.close()

    soup = BeautifulSoup(source, "lxml", from_encoding='utf-8')
    table_div = soup.find('div',{'class':'meal_box'})
    tr = table_div.find_all('tr')
    while today < 7:
            td = tr[today + 3].find_all('td')
            breakfast=td[1].text
            lunch=td[2].text
            dinner=td[3].text
            today = today + 1
            if breakfast == '\n\n\n':
               breakfast = '\n ※ 우리학교 학식데이터는 월요일 아침 9시30분 이후에 업데이트 됩니다. ㅜㅜ'
            if lunch == '\n\n\n':
               lunch = '\n ※ 우리학교 학식데이터는 월요일 아침 9시 30분 이후에 업데이트 됩니다. ㅜㅜ'
            if dinner == '\n\n\n':
               dinner = '\n ※ 아직 학식데이터를 학교에서 올리지 않았어요 ㅜㅜ'

            create_menu_db_table(day[today-1], '아침', breakfast)       
            create_menu_db_table(day[today-1], '점심', lunch)
            create_menu_db_table(day[today-1], '저녁', dinner)
   # create_menu_db_table('test','조식', breakfast)
    return JsonResponse({'status' : 'crawled'})

def create_menu_db_table(day, time, menu):
    Menu.objects.create(
            day=day,
            time=time,
            menu=menu
     )

def flush_menu_db():
    menu_db = Menu.objects.all()
    menu_db.delete()
