import threading
import time


g_num=0
mutex=threading.Lock()#global dont need to change
def test1(temp):
    global g_num#define g_num as global
    mutex.acquire()
    for i in range(temp):
        g_num += 1
    mutex.release()
    print('---1:{}---'.format(g_num))



def test2(temp):
    global g_num
    mutex.acquire()
    for i in range(temp):
        g_num += 1
    mutex.release()
    print('---2:{}---'.format(g_num))


def  main():
    t1=threading.Thread(target=test1,args=(1000000,))


    t2=threading.Thread(target=test2,args=(1000000,))
    t1.start()
    #in this case t2 is waiting until t1 has finished its routie
    t2.start()

    time.sleep(2)
    print('---main---:{}'.format(g_num))
#     ---1:1000000---
# ---2:2000000---
# ---main---:2000000



if __name__ == "__main__":
    main()
