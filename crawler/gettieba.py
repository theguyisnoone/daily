import urllib
import ssl
#cancel ssl verify
ssl._create_default_https_context = ssl._create_unverified_context

def loadPage(fullurl,filename):
    print('now downloading'+filename)
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    request=urllib.request.Request(fullurl,headers=headers)
    response=urllib.request.urlopen(request)
    a=response.read()#byte
    #return string..
    return str(a,encoding='utf-8')

def writeFile(html,filename):
    print('now saving'+filename)
    with open(filename,'w') as f:
        f.write(html)
    print('-' * 20)


def tiebaSpider(url,beginPage,endPage):
    for page in range(beginPage,endPage+1):
        pn=(page -1) *50

        filename ='>>>'+str(pn)+'page'
        fullurl=url+"&ie=utf-8&pn="+str(pn)

        html=loadPage(fullurl,filename)
        writeFile(html,filename)



def main():
    kw=input('tieba name:')
    beginPage=int(input('from:'))
    endPage=int(input('to:'))

    url="http://tieba.baidu.com/f?"
    key=urllib.parse.urlencode({'kw':kw})

    url=url+key
    tiebaSpider(url,beginPage,endPage)


if __name__ =='__main__':
    main()
