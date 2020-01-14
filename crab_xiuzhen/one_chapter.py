from bs4 import BeautifulSoup
import requests

url = "http://www.biquge.info/26_26516/"
def getinnerhtml(data):
    return data[data.find(">") + 1:data.rfind("</")]

def getOneChapter(htmlhandle):
	soup = BeautifulSoup(htmlhandle,'html.parser')
	content = soup.select_one('#content')
	s = str(content)
	s_replace = s.replace('<br/>', "\r\n")
	c_soup = BeautifulSoup(s_replace,'html.parser')
	final = c_soup.text
	return final

def crabOne(t):
	url1 = url + t['link']
	title = t['title']
	print('loading', title, url1)
	kv = {'user-agent':'Mozilla/5.0'}
	r = requests.get(url1, headers=kv)
	r.encoding = r.apparent_encoding
	chapter = getOneChapter(r.text)
	# print(chapter)
	if len(chapter)<10:
		print(r)
	return (title,chapter)