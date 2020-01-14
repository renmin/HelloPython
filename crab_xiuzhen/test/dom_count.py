import sys
from bs4 import BeautifulSoup

start = 0
stop = start + 100
fname = './crab_xiuzhen/result/%d-%d.txt' % (start + 1,stop)
print(fname)

def getinnerhtml(data):
    return data[data.find(">") + 1:data.rfind("</")]
	
file = './crab_xiuzhen/test/xiuzhen.html'
# print(file)
fopen = open(file, 'r', encoding='utf-8')
htmlhandle = fopen.read()
fopen.close()
soup = BeautifulSoup(htmlhandle,'html.parser')
# item_list = soup.find_all('div',attrs={'id':'content'})
# for item in item_list:
	# print(item.text)
content = soup.select_one('#content')
s = str(content)
s_replace = s.replace('<br/>', "\r\n")
s_replace = getinnerhtml(s_replace)
# print(s_replace)

c_soup = BeautifulSoup(s_replace,'html.parser')

final = c_soup.text
print(final)


fout = open('./crab_xiuzhen/test/test.txt','w',encoding = 'utf-8')
fout.write(final+'\n')
fout.close()