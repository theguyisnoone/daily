#coding=utf-8

import requests

response = requests.get('http://www.sina.com')

print(response.request.headers)

print(response.text)
