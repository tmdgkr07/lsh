

import json
from collections import OrderedDict
from bs4 import BeautifulSoup
from urllib.request import urlopen

f = open("haksik.json","w")
f.close()
day = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
today = 0



html = urlopen('http://www.kopo.ac.kr/gwangju/content.do?menu=4636')
source = html.read()
html.close()

soup = BeautifulSoup(source, "lxml")
table_div = soup.find('div',{'class':"meal_box"})
tables = table_div.find_all("table")
menu_table = tables[1]
tr = menu_table.find_all('tr')

while today < 7 :
    meal = tr[today+1]
    td = meal.find_all('span')
#print(td)

#td =  td.replace('<span>','').replace('</span>','').replace('<td><script>document.write(getDay2(','').replace('<td>','').replace('</td>','').replace(')','').replace('</script><br/>','')




   # file_data = OrderedDict()

    
    file_data = {day[today]:[td[0].text,td[1].text,td[2].text]}
    
    
    today = today+1




#make_file
    print(json.dumps(file_data, ensure_ascii=False, indent="\t"))
    with open('haksik.json', 'a+', encoding="utf-8") as f:
         json.dump(file_data, f, ensure_ascii=False, indent="\t")
