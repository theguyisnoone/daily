from gevent import monkey
import gevent
import urllib.request

monkey.patch_all()#耗时caoz

def my_download(url):
    print('get:{}'.format(url))
    resp=urllib.request.urlopen(url)
    data=resp.read()
    print('{} bytes received from {} '.format(len(data),url))



gevent.joinall([
gevent.spawn(my_download,'http://www.baidu.com/'),
gevent.spawn(my_download,'http://www.itcast.cn/'),
gevent.spawn(my_download,'http://www.baidu.com/'),
])
