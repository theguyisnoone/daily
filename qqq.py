import multiprocessing

def put_it_in(q):
    data=[1,2,3,4]
    for i in data:
        q.put(i) #put in
    print('------put in------')


def take_it_out(q):
    # receive=[]
    receive=list()#empty list better than []
    while True:
        temp=q.get()
        receive.append(temp)

        if q.empty():
            break
    print(receive)


def main():
    q=multiprocessing.Queue()#q quoted by t1,t2
    t1=multiprocessing.Process(target=put_it_in,args=(q,))
    t2=multiprocessing.Process(target=take_it_out,args=(q,))
    t1.start()
    t2.start()

if  __name__ == "__main__":
    main()
