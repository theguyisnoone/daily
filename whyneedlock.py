import threading
import time

'''so much resource cpu need to frequently change them so ...
maybe turn into chaos'''
g_num=0

def test1(temp):
    global g_num#define g_num as global
    for i in range(temp):
        g_num += 1
    print('---1:{}---'.format(g_num))



def test2(temp):
    global g_num
    for i in range(temp):
        g_num += 1
    print('---2:{}---'.format(g_num))


def  main():
    t1=threading.Thread(target=test1,args=(100000000,))


    t2=threading.Thread(target=test2,args=(100000000,))
    t1.start()
    t2.start()
#     ---main---:28622471
# ---1:126803457---
# ---2:127107718---
#turn into chaos so we need chaos cause so much resource cpu need to frequently
#change process
    time.sleep(5)
    print('---main---:{}'.format(g_num))



if __name__ == "__main__":
    main()
