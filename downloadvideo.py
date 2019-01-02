from gevent import monkey
import gevent
import urllib.request

monkey.patch_all()#耗时操作 像io处理

def my_download(filename,url):
    print('get:{}'.format(url))
    resp=urllib.request.urlopen(url)
    data=resp.read()
    print('{} bytes received from {} '.format(len(data),url))

    with open(filename,'wb') as f:
        f.write(data)

    print('{} bytes received from {} '.format(len(data),url))

gevent.joinall([
gevent.spawn(my_download,'1.mp4','https://www.bilibili.com/video/av1665556/'),
gevent.spawn(my_download,'2.mp4','https://www.bilibili.com/video/av1665556/'),

])
