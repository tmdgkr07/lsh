import requests 


appKey = "7f33452d-fe4f-4cac-85c3-3c7c88c6f1f5"

weather = 'weather'
# 현재 날씨(시간별)
url_hourly = "http://api2.sktelecom.com/weather/current/hourly"
# 현재 날씨(분별)
url_minutely = "http://api2.sktelecom.com/weather/current/minutely"

headers = {'Content-Type': 'application/json; charset=utf-8',
           'appKey': appKey}

def hourly():
    
    humidity =request['humidity']

    print(humidity)



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

def create_menu_db_table(place, status, temperature):
    Weather.objects.create(
            place=place,
            status=status,
            temperature = temperature
    )

def flush_menu_db():
    Weather_db = Weather.objects.all()
    Weather_db.delete()

if __name__ == '__main__':
    #city = '경기'  #'도' 나 '시'는 빼고 넣는다.
    #county = '김포시' #시 or 구
    #village = '장기동' #동
    # 시간별 (기본)
    requestCurrentWeather('광주','북구','운암2동')

