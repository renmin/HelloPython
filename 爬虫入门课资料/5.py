import requests
from bs4 import BeautifulSoup

kv = {'user-agent':'Mozilla/5.0'}


r = requests.get("https://www.xfz.cn/",headers=kv)

r.encoding = r.apparent_encoding

soup = BeautifulSoup(r.text,'lxml')
item_list = soup.find_all('a',attrs={'class':'li-container'})

# 技能六
for item in item_list:
    print (item['href'])
