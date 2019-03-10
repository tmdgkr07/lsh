
from bs4 import BeautifulSoup
from urllib.request import urlopen


html =urlopen('http://www.kopo.ac.kr/gwangju/content.do?menu=4636')
source= html.read()
html.close()

soup = BeautifulSoup(source, "lxml")
table_div = soup.find('div',{'class':'meal_box'})
td = table_div.find_all('td')


tds = td[4].text
mon = td[3], td[4].span, td[5].span, td[6].span 
tue = td[7], td[8].span, td[9].span, td[10].span 
wed = td[11], td[12].span, td[13].span, td[14].span
thu = td[15], td[16].span, td[17].span, td[18].span
fri = td[19], td[20].span, td[21].span, td[22].span
sat = td[23], td[24].span, td[25].span, td[26].span
sun = td[27], td[28].span, td[29].span, td[30].span


mon = str(mon).replace('<td>','').replace('<script>','').replace('document.write','').replace('(','').replace(')','').replace('<span>','').replace('0','').replace('getDay2','').replace('2018','').replace(':','').replace('-','').replace('1','').replace('7','').replace('6','').replace('5','').replace('4','').replace('3','').replace('2','').replace('9','').replace('8','').replace('</span>','')
print(tds)



