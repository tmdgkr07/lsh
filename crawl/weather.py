from bs4 import BeautifulSoup
import urllib.request

def get(max_count= 1):
    base_url =  "~/crawl"

    count = 1
    while count <= max_count:
        html = urllib.request.urlopen('https://m.weather.naver.com/m/main.nhn?regionCode=01150101&where=m&sm=mtp_clk.weather')
        source = html.read()
        html.close()
	soup = B

        img = soup.find("img")
	img_src = img.get("src")
	img_url = base_url + img_src

	print(img_src)
	print(img_url)

get(1)
