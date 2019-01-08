import requests

proxies = {
  "http": "http://12.34.56.79:9527",
  "https": "http://12.34.56.79:9527",
}

proxy = { "http": "mr_mao_hacker:sffqry9r@61.158.163.130:16816" }

url="http://www.baidu.com"

response=requests.post(url,proxies=proxy)

print(response.text)

#代理不通
