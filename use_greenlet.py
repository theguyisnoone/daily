from greenlet import greenlet
import time
'''yield'''
def test1():
    while True:
        print('----test1----')
        gr2.switch()
        # yield#make it become a generator
        time.sleep(0.1)

def test2():
    while True:
        print('----test2----')
        gr1.switch()
        # yield#make it become a generator
        time.sleep(0.1)


gr1=greenlet(test1)
gr2=greenlet(test2)
gr1.switch()
#互相切换
