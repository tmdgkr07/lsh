
from bs4 import BeautifulSoup
from urllib.request import urlopen


today = 0
day = [ 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
html =urlopen('http://www.kopo.ac.kr/gwangju/content.do?menu=4636')
source= html.read()
html.close()

soup = BeautifulSoup(source, "lxml")
table_div = soup.find('div',{'class':'meal_box'})
tr = table_div.find_all('tr')
while today < 7:
        td = tr[today + 3].find_all('td')
        breakfast=td[1].text
        today = today + 1
        create_menu_db_table(day[today-1], '조식', breakfast)
        

