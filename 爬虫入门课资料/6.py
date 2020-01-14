import requests
from bs4 import BeautifulSoup
import json

kv = {'user-agent':'Mozilla/5.0'}

# 技能七
r = requests.get("https://www.xfz.cn/api/website/articles/?p=100&n=20&type=",headers=kv)

r.encoding = r.apparent_encoding

text = r.text.encode('utf-8').decode('unicode-escape')

dict = json.loads(text)

for i in dict['data']:
    
    print (i['title'])