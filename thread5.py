import threading
import time


def test1():
    for i in range(5):
        print('xxx {}'.format(i))
        time.sleep(1)




def main():
    print('>>>before create:')
    print(threading.enumerate())

    t1=threading.Thread(target=test1)

    print('>>>after create:')
    print(threading.enumerate())

    print('>>>before start:')
    print(threading.enumerate())

    t1.start()

    print('>>>after start:')
    print(threading.enumerate())



    print(threading.enumerate())








if __name__  == "__main__":
    main()
