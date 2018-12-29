import threading
import time

'''all thread share same global'''
g_num=100

def test1():
    global g_num#define g_num as global
    g_num += 1
    print('---1:{}---'.format(g_num))



def test2():
    print('---2:{}---'.format(g_num))


def  main():
    t1=threading.Thread(target=test1)
    t1.start()
    time.sleep(1)
    t2=threading.Thread(target=test2)
    t2.start()
    print('---main---:{}'.format(g_num))



if __name__ == "__main__":
    main()
