import os
import multiprocessing
import time

def test1(name,age,**kwargs):
    for i in range(10):
        print('my name:{},my age:{},pid:{}'.format(name,age,os.getpid()))
        print(kwargs)
        time.sleep(0.2)


def main():

    p1=multiprocessing.Process(target=test1,args=('huhuuh',18),kwargs={'jaja':'lala'})
     #kwargs is dict
    p1.start()
    time.sleep(1)
    p1.terminate()#in 1 second only can run fifth boom!!
    print('wait')
    p1.join(5)#??




if __name__ == '__main__':
    main()
