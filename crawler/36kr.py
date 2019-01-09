import requests
import re

class Duanzi_spider(object):
    def __init__(self):
        self.index_url="https://36kr.com/" #list_5_x
        self.headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    def load_Page(self,url):
        print(url)
        response=requests.get(url,headers=self.headers)
        return response.content.decode()




    def get_content(self,html_str):
        pa=re.compile(r'"template_title":"(.*?)",.*?,"summary":(.*?)。', re.S)
        content_list = pa.findall(html_str)
        print('first>>>')
        print(content_list)
        # return result

    # def save_file(self,result,filename):
    #     with open(filename,'w') as f:
    #         for temp in result:
    #             s=''.join(temp)#list --> string
    #             f.write(s+'\n')
    #             f.write('-------'+'\n')
    #         print('oover')


    def run(self):
        html_str=self.load_Page(self.index_url)
        result=self.get_content(html_str)
        # filename='neihan%d.txt'%i
        # filename='36kr.txt'
        # self.save_file(result,filename)







# t1=Duanzi_spider('http://www.neihan8.com/')
# t1.load_Page('http://www.neihan8.com/')

if __name__ == "__main__":
    t1=Duanzi_spider()
    t1.run()
