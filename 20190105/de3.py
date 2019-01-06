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






test1(100)
test1(100,200)
test1(100,200,m=100)
