import threading
import time

'''
循环查看当前线程
当线程只剩下主线程时 break
'''
def test1():
    for i in range(5):
        print('xxx {}'.format(i))
        time.sleep(1)
    #函数执行结束，子线程结束    


def test2():
    for i in range(10):
        print('yyy {}'.format(i))
        time.sleep(1)


def main():
    t1=threading.Thread(target=test1)
    t2=threading.Thread(target=test2)
    t1.start()
    t2.start()

    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) <=1 : #only main Thread
            print('only main thread! over now')
            break
        time.sleep(1)




if __name__  == "__main__":
    main()
