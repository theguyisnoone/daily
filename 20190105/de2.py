def set_fuc(func): #闭包
    def call_fuc(a): #a receive num
        print('halo')
        func(a)
    return call_fuc


@set_fuc
def test1(num):
    print('hi {}'.format(num))

@set_fuc
def test2(num):
    print('kkk {}'.format(num))

test1(100)

test2(200)
