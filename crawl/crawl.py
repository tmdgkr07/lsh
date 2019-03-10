
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://www.kopo.ac.kr/gwangju/content.do?menu=4636')
source = html.read()
html.close()

print(source)

