

import requests

#代码片
#   web client confirm
# auth={'lee','123'}
# url='http://192.168.199.107'
# response=requests.get(url,auth=auth)
#
# print(response.text)

#cookies
response =requests.get('https://www.baidu.com')

cookiejar=response.cookies

#cookies --> dict
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

print(cookiejar)
print(cookiedict)
