import requests

# 技能3-1
kv = {'user-agent':'Mozilla/5.0'}

r = requests.get("https://www.douban.com/note/742422285",headers = kv)

print (r.status_code)





