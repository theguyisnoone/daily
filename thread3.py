import threading
import time

'''利用time.sleep()让某些程序优先执行'''


def test1():
    for i in range(5):
        print('xxx')

def test2():
    for i in range(5):
        print('yyy')



def main():
    t1=threading.Thread(target=test1)
    t2=threading.Thread(target=test2)
    t1.start()
    time.sleep(1)#let t1 first finish
    t2.start()
    time.sleep(1)#let t2 finish
    print(threading.enumerate())



if __name__  == "__main__":
    main()
