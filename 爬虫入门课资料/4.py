import requests
from bs4 import BeautifulSoup

kv = {'user-agent':'Mozilla/5.0'}


for i in range(1,11):

    r = requests.get("https://price.pcauto.com.cn/comment/sg2734/"+"p"+str(i)+".html")

    r.encoding = r.apparent_encoding

	# 技能四
    soup = BeautifulSoup(r.text,"html.parser")
    item_list = soup.find_all('div',attrs={'class':'conLit youdian'})

	# 技能五
    for item in item_list:
        print (item.find('span').text)


#title = li.find('a')['href']
#fout.write(title+'\n')
#fout = open('title.txt','w',encoding = 'utf-8')
#fout.close()
    
    
    
    
    
    
    