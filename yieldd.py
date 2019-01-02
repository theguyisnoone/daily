import time
def test1():
    while True:
        print('----test1----')

        yield#make it become a generator
        time.sleep(0.1)

def test2():
    while True:
        print('----test2----')

        yield#make it become a generator
        time.sleep(0.1)


def main():
    t1=test1()
    t2=test2()
    for i in range(10):
        next(t1)
        next(t2)




if __name__ == '__main__':
    main()
