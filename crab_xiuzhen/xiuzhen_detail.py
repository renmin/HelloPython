import requests
from bs4 import BeautifulSoup
import numpy as np
import one_chapter
import time





url = "http://www.biquge.info/26_26516/"
filename = '修真聊天群titles.npy'

titles = np.load(filename)

print('加载标题和链接，共',len(titles),'个')


start = 300
stop = start + 100
def crabRang(start,stop):
	allText = ""
	for i in range(start, stop):
		t = titles[i]
		(title, chapter) = one_chapter.crabOne(t)
		
		length = len(chapter)
		print (length)
		retry = 1
		while (length < 10 and retry < 3):
			print('Retry',retry)
			time.sleep(2)
			(title, chapter) = one_chapter.crabOne(t)
			retry += 1
		if length < 10:
			print (i, 'Failed')
		else:
			print ('OK')

		allText += title + '\n\n'
		allText += chapter + '\n\n'

	fname = './crab_xiuzhen/result/%d-%d.txt' % (start + 1, stop)

	fout = open(fname,'w',encoding = 'utf-8')
	fout.write(allText+'\n')
	fout.close()

# (title,chapter) = one_chapter.crabOne(titles[97])

# print(title,chapter)

crabRang(start,stop)

