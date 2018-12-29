import os
import multiprocessing

def test1():
    while True:
        print('ttttttttssssss')
    print('my pid:{}'.format(os.getpid()))

def main():
    print(' main pid:{}'.format(os.getpid()))
    p1=multiprocessing.Process(target=test1)

    p1.start()


if __name__ == '__main__':
    main()
