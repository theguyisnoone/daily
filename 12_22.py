import time
import threading

"""线程 """
def sing():
    for i in range(5):
        print('singing')
        time.sleep(1)


def dance():
    for i in range(5):
        print('dancing')
        time.sleep(1)


def main():
    # 单线程
    # sing()
    # dance()
    t1=threading.Thread(target=sing)#创建t1实例对象
    t2=threading.Thread(target=dance)
    t1.start()#t1的主线程 生出了sing这个子线程
    #21，23 创建独立任务
    t2.start()#t2的主线程 生出了dance这个子线程

    #子线程结束后主线程才结束



if __name__ == '__main__':
    main()
