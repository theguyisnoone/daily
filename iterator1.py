from collections import Iterable,Iterator


class test(object):
    def __init__(self):
        #create empty list
        self.name=list()

    def add(self,val):
        #append some cuti cuti
        self.name.append(val)


    def __iter__(self):
        #only have this ,object can be iterate
        return  titerator(self)


class titerator(object):
    def __init__(self,obj):#receive object created by test  then we can loop by using next
        self.obj=obj
        self.current_position=0#class attribute

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_position < len(self.obj.name):
            #next like one time for
            item=self.obj.name[self.current_position]
            self.current_position += 1
            return item
        else:
            raise StopIteration



def main():
    t=test()
    t.add('lee')
    t.add('jaja')
    t.add('king')
    t.add('jajajajaj ')
    for i in t:
        print(i)





if __name__ == '__main__':
    main()
