import threading
import time

'''share data use args'''
g_nums=[11,22]

def test1(temp):#get one attribute
    g_nums.append(33)#tuple cant be changed so its global
    print('---1:{}---'.format(g_nums))



def test2(temp):
    print('---2:{}---'.format(g_nums))


def  main():
    t1=threading.Thread(target=test1,args=(g_nums,))#args must be tuple
    t1.start()
    time.sleep(1)
    t2=threading.Thread(target=test2,args=(g_nums,))
    t2.start()
    print('---main---:{}'.format(g_nums))



if __name__ == "__main__":
    main()
