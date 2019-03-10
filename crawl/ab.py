
f = open("haksik.txt", 'w')

from bs4 import BeautifulSoup
from urllib.request import urlopen


html = urlopen('http://www.kopo.ac.kr/gwangju/content.do?menu=4636')
source = html.read()
html.close()

soup = BeautifulSoup(source, "lxml")
table_div = soup.find('div',{'class':"meal_box"})
tables = table_div.find_all("table")
menu_table = tables[1]
td = menu_table.find_all('td')


##morning =  td[:].replace('<td><script>document.write(getDay2(','').replace('<td>','').replace('</td>','').replace('<span>','').replace('</span>','') 
lunch = td[2].span
dinner = td[3].span
mon = td[:]
mon = str(mon).replace('<span>','').replace('</span>','').replace('<td><script>document.write(getDay2(','').replace('<td>','').replace('</td>','').replace(')','').replace('</script><br/>','')


print(mon,"\n",lunch.text)
f.write(mon)
f.close()
