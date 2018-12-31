# from collections import Iterable,Iterator

'''模糊了创建列表的事情 删除了list append 的东西
   接受长度  第一个返回的值是a  然后给a变换
   再来个current_position 控制长度  

'''
class fibonacci(object):
    def __init__(self,len):
        #create empty list
        self.len=len #fibonacci's length
        self.current_position=0
        self.a=0 #first
        self.b=1 #second


    def __iter__(self):
        return  self

    def __next__(self):
        if self.current_position < self.len:
            #next like one time for
            item = self.a
            self.a,self.b=self.b,self.a+self.b
            self.current_position += 1
            return item
        else:
            raise StopIteration


def main():
    fi=fibonacci(10)
    for num in fi:
        print(num)





if __name__ == '__main__':
    main()
