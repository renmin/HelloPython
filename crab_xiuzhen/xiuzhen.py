import requests
from bs4 import BeautifulSoup
import numpy as np

url = "http://www.biquge.info/26_26516/"
filename = '修真聊天群titles.npy'
titles = []


kv = {'user-agent':'Mozilla/5.0'}
r = requests.get(url, headers=kv)
r.encoding = r.apparent_encoding

soup = BeautifulSoup(r.text)

dd_list = soup.find_all('dd')

for dd in dd_list:
	link = dd.find('a')
	title = {
		'title':link['title'],
		'link': link['href']
	}
	titles += [title]

np.save(filename, titles) 


