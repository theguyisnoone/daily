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
gevent.spawn(my_download,1.jpg,'http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Farchive\u002Fb9e8630d22c17f047ba9f3ea2a2c426070f4d9fe.jpg'),
gevent.spawn(my_download,2.png,'http:\u002F\u002Fi0.hdslb.com\u002Fbfs\u002Farchive\u002F047cd6057bdfe75c818c08d0b3563afca46f7c5a.png'),

])
