import requests
import re

class Duanzi_spider(object):
    def __init__(self):
        self.index_url="https://www.neihan8.com/article/list_5_%d.html" #list_5_x
        self.headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    def load_Page(self,url):
        print(url)
        response=requests.get(url,headers=self.headers)
        return response.content.decode('gbk')


    def get_content(self,html_str):
        pa=re.compile(r'<a\shref="/article/\d+\.html">(.*?)</a>.*?<div\sclass="f18 mb20">(.*?)</div>', re.S)
        content_list = pa.findall(html_str)
        print('first>>>')
        result=list()
        for i in content_list:#i one of the list string
            temp=list()
            for j in i:
                j = re.sub(r"[<b>|</b>|<br />|<br>|<p>|</p>|\\u3000|\\r\\n|\s]","",j)
                j = re.sub(r"[&ldqo;]|[&helli;]","",j)
                temp.append(j)
                print(temp)
            result.append(temp)
            a=len(result)
        return result

    def save_file(self,result,filename):
        with open(filename,'w') as f:
            for temp in result:
                s=''.join(temp)#list --> string
                f.write(s+'\n')
                f.write('-------'+'\n')
            print('oover')


    def run(self):

        #loop
        i=1
        while True:
            html_str=self.load_Page(self.index_url%i)
            result=self.get_content(html_str)
            filename='neihan%d.txt'%i
            self.save_file(result,filename)
            print('enter continue')
            print('quit to quit')
            command=input('>>>')
            if command == 'quit':
                break
            i += 1


# t1=Duanzi_spider('http://www.neihan8.com/')
# t1.load_Page('http://www.neihan8.com/')

if __name__ == "__main__":
    t1=Duanzi_spider()
    t1.run()
