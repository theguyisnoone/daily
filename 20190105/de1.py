def set_fuc(func): #闭包
    def call_fuc():
        print('halo')
        func()
    return call_fuc


@set_fuc
def test():
    print('hi')


test()
