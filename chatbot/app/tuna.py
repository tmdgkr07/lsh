#-*- coding:utf-8 -*-
import requests
#from app.models import Weather
from django.utils.datastructures import MultiValueDictKeyError
# SK Planet에서 키 요청 받아야 함.
# https://developers.skplanetx.com/develop/
# 앱 등록 및 키 발급

appKey = "7f33452d-fe4f-4cac-85c3-3c7c88c6f1f5"

weather = 'weather'
# 현재 날씨(시간별)
url_hourly = "http://api2.sktelecom.com/weather/current/hourly"
# 현재 날씨(분별)
url_minutely = "http://api2.sktelecom.com/weather/current/minutely"

headers = {'Content-Type': 'application/json; charset=utf-8',
           'appKey': appKey}

#현재 날씨(시간별)
#def minutely(request):
 #   humidity = request['humidity']

 #   print(humidity)
def minutely(request):
    humidity = request['humidity']


    temperature_tmax = request['temperature']['tmax']
    temperature_tc   = request['temperature']['tc']
    sky_code = request['sky']['code']
    sky_name = request['sky']['name']
    # 발표 시간
      # 시, 도
    e='현재온도: '+temperature_tc + '\n최고온도: '+temperature_tmax + '\n습도: '+humidity + '\n하늘: '+sky_name
    #create_weather_db_table(humidity, humidity, humidity)
    print(e)
    print(humidity)
   # print(hourly_weather)
    f = open('/home/lsh/chatbot/app/test.txt', 'wt', encoding="utf-8")
    f.write(e)
    f.close()
    f = open('/home/lsh/chatbot/app/code.txt', 'wt', encoding='utf-8')
    f.write(sky_code)
    f.close()

    print(humidity)

def hourly(request):
    
    
    # print(weather)
    # 상대 습도
    
    humidity     = request['humidity']
    timeRelease = request['timeRelease'] 
    temperature_tmax = request['temperature']['tmax']
    temperature_tc   = request['temperature']['tc']
    sky_code = request['sky']['code']
    sky_name = request['sky']['name']
    # 발표 시간
      # 시, 도
    e='현재온도: '+temperature_tc + '\n최고온도: '+temperature_tmax + '\n습도: '+humidity + '\n하늘: '+sky_name+'\n발표시간: '+timeRelease
    #create_weather_db_table(humidity, humidity, humidity)
    
    print(humidity)
   # print(hourly_weather)
    # 기온 정보
    # 오늘의 최고기_tmin = weather['temperature']['tmin']

    # 낙뢰유무(해당 격자 내)
    # - 0: 없음
    # - 1: 있음
    # 강수량
    # 강수형태코드
    # - 0: 현상없음 → rain(sinceOntime) 사용
    # - 1: 비       → rain(sinceOntime) 사용
    # - 2: 비/눈 → precipitation(sinceOntime) 사용
    # - 3: 눈    → precipitation(sinceOntime) 사 = weather['wind']['wspd']

    # 하늘 상태 정보
    # 하늘상태코드명
    # - SKY_A01: 맑음
    # - SKY_A02: 구름조금
    # - SKY_A03: 구름많음
    # - SKY_A04: 구름많고 비
    # - SKY_A05: 구름많고 눈
    # - SKY_A06: 구름많고 비 또는 눈
    # - SKY_A07: 흐림
    # - SKY_A08: 흐리고 비
    # - SKY_A09: 흐리고 눈
    # - SKY_A10:  흐리고 비 또는 눈
    # - SKY_A11: 흐리고 낙뢰
    # - SKY_A12: 뇌우, 비
    # 기온 정보
    # 오늘의 최고
    # 낙뢰유무(해당 격자 내)
    # - 0: 없음
    # - 1: 있음
    # 강수량
    # 강수형태코드
    # - 0: 현상없음 → rain(sinceOntime) 사용
    # - 1: 비       → rain(sinceOntime) 사용
    # - 2: 비/눈 → precipitation(sinceOntime) 사용
    # - 3: 눈    → precipitation(sinceOntime) 사용
    # - if type=0/1/2 → 강우량 (mm)
    # - if type=3     → 적설량 (
    # 하늘 상태 정보
    # 하늘상태코드명
    # - SKY_A01: 맑음
    # - SKY_A02: 구름조금
    # - SKY_A03: 구름많음
    # - SKY_A04: 구름많고 비
    # - SKY_A05: 구름많고 눈
    # - SKY_A06: 구름많고 비 또는 눈
    # - SKY_A07: 흐림
    # - SKY_A08: 흐리고 비
    # - SKY_A09: 흐리고 눈
    # - SKY_A10:  흐리고 비 또는 눈
    # - SKY_A11: 흐리고 낙뢰
    # - SKY_A12: 뇌우, 비
    # - SKY_A13: 뇌우, 눈
    # - SKY_A14: 뇌우, 비 또

def requestCurrentWeather(city, county, village, isHourly = True):
    params = { "version": "1",
                "city": city,
                "county": county,
                "village": village }
    if isHourly:
        response = requests.get(url_hourly, params=params, headers=headers)
    else:
        response = requests.get(url_minutely, params=params, headers=headers)

    if response.status_code == 200:
        response_body = response.json()
    #    print(response_body)
    #    print(humidity)
       #날씨 정보
        try:
            if isHourly:
                weather_data = response_body['weather']['hourly'][0]
            else:
                weather_data = response_body['weather']['minutely'][0]

            if isHourly:
                hourly(weather_data)
            else:
                minutely(weather_data)
        except:
            pass
    else:
        pass
        #에러

if __name__ == '__main__':
    #city = '경기'  #'도' 나 '시'는 빼고 넣는다.
    #county = '김포시' #시 or 구
    #village = '장기동' #동
    # 시간별 (기본)
     requestCurrentWeather('광주','북구','운암2동')
     requestCurrentWeather('광주','북구','운암2동', False)
    
# print(requestCurrentWeather('광주','북구','운암2동'))
   #print(e)
    
