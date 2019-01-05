#class  occupy a lot of resource
class line(object):
    def __init__(self,k,b):
        self.k=k
        self.b=b


    def __call__(self,x):#!
        print(self.k * x +self.b)


line1=line(1,2)
line1(0)
line1(1)
line1(2)

line2=line(11,22)
line2(0)
line2(1)
line2(2)

print('*' * 50)
#闭包
def line2(k,b):
    def create(x):
        print(k*x + b)
    return create #!!    
line2_1=line2(1,2)
line2_1(0)
line2_1(1)
line2_1(2)
