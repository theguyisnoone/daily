import requests


formdata={"type":"AUTO",
    "i":"i love python",
    "doctype":"json",
    "xmlVersion":"1.8",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_ENTER",
    "typoResult":"true"}

url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

response=requests.post(url,data=formdata,headers =headers)

print(response.text)

print(response.json())

'''
{"type":"EN2ZH_CN","errorCode":30,"elapsedTime":0,"translateResult":[[{"src":"您的请求来源非法，商业用途使用请关注有道翻译API官方网站\u201C有道智云\u201D: http:\/\/ai.youdao.com","tgt":"您的请求来源非法，商业用途使用请关注有道翻译API官方网站\u201C有道智云\u201D: http:\/\/ai.youdao.com"}]]}

{'type': 'EN2ZH_CN', 'errorCode': 30, 'elapsedTime': 0, 'translateResult': [[{'src': '您的请求来源非法，商业用途使用请关注有道翻译API官方网站“有道智云”: http://ai.youdao.com', 'tgt': '您的请求来源非法，商业用途使用请关注有道翻译API官方网站“有道智云”: http://ai.youdao.com'}]]}
'''
