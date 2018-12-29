
import os
from multiprocessing import Pool,Manager
import time


def write(q):
    print('now write pid:{}'.format(os.getpid()))
    for i in 'lm lee':
        q.put(i)
    print('finish write pid:{}'.format(os.getpid()))

def read(q):
    print('now read pid:{}'.format(os.getpid()))
    over=list()
    for i in range(q.qsize()):#qsize()!!
        temp=q.get(i)
        over.append(temp)
    print(over)
    print('finish read,its over now. pid:{}'.format(os.getpid()))


if __name__ == '__main__':
    #record main process pid
    print('main process pid:{}'.format(os.getpid()))
    #create Pool
    po=Pool()#we just do one thing write all first and read all first
    #create one queue item
    q=Manager().Queue()#if we create queue in pool
    #we can write in and read out


    #first write
    po.apply_async(write,(q,))
    #wait
    time.sleep(1)
    #second read
    po.apply_async(read,(q,))
    #close Pool
    po.close()
    #wait child finish
    po.join()
    #reshow main process pid
    print('main process pid:{}'.format(os.getpid()))
