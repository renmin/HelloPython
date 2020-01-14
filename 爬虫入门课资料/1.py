import requests

# 技能一
r = requests.get("https://www.baidu.com/")

# 技能二
r.encoding = r.apparent_encoding

print (r.status_code)






