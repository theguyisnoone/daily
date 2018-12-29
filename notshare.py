import os
import multiprocessing
import time

nums=[11,22]#global
def test1():#write
    print('now nums:{}'.format(nums))
    for i in range(3):
        nums.append(i)
        print('after add:{} '.format(nums))
        time.sleep(1)

def test2():#read
    print('read nums:{}'.format(nums))


def main():

    p1=multiprocessing.Process(target=test1)
    p2=multiprocessing.Process(target=test2)
    p1.start()
    p1.join()#wait p1 finish first
    p2.start()


'''we not share global in process'''

# now nums:[11, 22]
# after add:[11, 22, 0]
# after add:[11, 22, 0, 1]
# after add:[11, 22, 0, 1, 2]
# read nums:[11, 22] 



if __name__ == '__main__':
    main()
