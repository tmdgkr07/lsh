from django.shortcuts import render
from django.http import JsonResponse
from app.models import Menu
from app.models import Weather
#from app.models import Weather
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.views.decorators.csrf import csrf_exempt
import json,datetime
from datetime import timedelta
from dateutil.relativedelta import *
import requests
import app.tuna

# Create your views here.

current_weather = ''

#-*- coding:utf-8 -*-


# SK Planet에서 키 요청 받아야 함.
# https://developers.skplanetx.com/develop/
# 앱 등록 및 키 발급
appKey = "7f33452d-fe4f-4cac-85c3-3c7c88c6f1f5"


# 현재 날씨(시간별)
url_hourly = "http://api2.sktelecom.com/weather/current/hourly"
# 현재 날씨(분별)
url_minutely = "http://api2.sktelecom.com/weather/current/minutely"

headers = {'Content-Type': 'application/json; charset=utf-8',
           'appKey': appKey}




def keyboard(request):

    return JsonResponse({
        'type': 'buttons',
        'buttons': ['오늘의 학식', '날 씨(BETA)','처음으로']
    })


@csrf_exempt
def message(request):
    f_weather = open('/home/lsh/chatbot/app/test.txt', 'r')
    hourly_weather = f_weather.read()
    f_weather.close()
    
    f_code = open('/home/lsh/chatbot/app/code.txt', 'r')
    sky_code = f_code.read()
    f_code.close()
   # today_weather = hourly(weather)
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
    if sky_code == 'SKY_A03':
        sky_code = 'sky_a03'
    if sky_code == 'SKY_A01':
        sky_code = 'sky_a01'

    if sky_code == 'SKY_A02':
        sky_code = 'sky_a02'

    if sky_code == 'SKY_A04':
        sky_code = 'sky_a04'

    if sky_code == 'SKY_A05':
        sky_code = 'sky_a05'

    if sky_code == 'SKY_A06':
        sky_code = 'sky_a06'

    if sky_code == 'SKY_A07':
        sky_code = 'sky_a07'

    if sky_code == 'SKY_A08':
        sky_code = 'sky_a08'

    if sky_code == 'SKY_A09':
        sky_code = 'sky_a09'

    if sky_code == 'SKY_A10':
        sky_code = 'sky_a10'

    if sky_code == 'SKY_A11':
        sky_code = 'sky_a11'

    if sky_code == 'SKY_A12':
        sky_code = 'sky_a12'

    if sky_code == 'SKY_A13':
        sky_code = 'sky_a13'

    if sky_code == 'SKY_A14':
        sky_code = 'sky_a14'




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
                  'buttons' : ['오늘의 학식', '날 씨(BETA)','처음으로']
                   }
                 })

    if content_name == '날 씨(BETA)':
        
        return JsonResponse({
                    
            'message':{
                    'photo': { 
                      'url': 'http://www.weatherplanet.co.kr/images/common/ico/weather/ico_b_' + sky_code + '.png',
                    'width': 640,
                   'height': 480}, 
                 'text': hourly_weather
            
                        },                     
                   


                'keyboard' : {
                'type' : 'buttons',
                'buttons' : ['오늘의 학식', '날 씨(BETA)','처음으로']

                 }})
        f.close()
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
           # create_menu_db_table('가','나', weather_data)
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

