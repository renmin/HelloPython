import requests

# 技能3-2
px = {'http':'114.239.253.223:9999'}

r = requests.get("https://item.jd.com/21848906495.html",proxies=px)

print (r.text)