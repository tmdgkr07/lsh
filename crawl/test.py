
from bs4 import BeautifulSoup
from urllib.request import urlopen


html = urlopen('http://dgucoop.dongguk.edu/store/store.php?w=4&l=2&j=0')
source = html.read()
html.close()

soup = BeautifulSoup(source, "lxml")
table_div = soup.find(id="sdetail")
tables = table_div.find_all("table")
menu_table = tables[1]
trs = menu_table.find_all('tr')

print(trs[2])
