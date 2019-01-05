x=300

def test1():
    x=200
    def test2():
        nonlocal x #闭包外的x
        print('x:{}'.format(x))
        x=100#局部变量
        print('x:%d'%x)

    return test2#返回test2的引用  加（）是test2的返回

t1=test1()
t1()
