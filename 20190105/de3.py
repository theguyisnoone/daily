def set_fuc(func): #闭包
    def call_fuc(*args,**kwargs): #a receive num
        print('halo')
        func(*args,**kwargs)
    return call_fuc


@set_fuc
def test1(num,*args,**kwargs):
    print('hi %d'%num)
    print('hi {}'.format(args))
    print('hi {}'.format(kwargs))






b=(100,200,300)
c={'m':100}
test1(*b,**c)
