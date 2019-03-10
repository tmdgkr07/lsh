
import requests

serviceKey = "MKX1Yi3xj%2FGRr%2B48GqbdzPATEKG7sIVOi4PQpHWzHsKCX%2FTJHbxTNzCJ1kSJoSPUbpiftFs%2FiroqMVdL1fZuWQ%3D%3D"

uri_bus = "http://api.gwangju.go.kr/json/arriveInfo"

headers = {'Content-Type': 'application/json; charset=utf=8',
           'serviceKey': serviceKey}

def bus(request):
    BUSSTOP_LIST = request['BUSSTOP_LIST']
    BUSSTOP_NAME = request['BUSSTOP_NAME']
    print(BUSSTOP_LIST, BUSSTOP_NAME)
def requestbusstop(BUSSTOP_ID, isbus= True):
    params = {"BUSSTOP_ID":BUSSTOP_ID}
    if isbus:
        response = requests.get(uri_bus, params=params, headers=headers)
    
    if response.status_code == 200:
        response_body = response.json()
        
if __name__ == '__main__':
    requestbusstop('2987')
