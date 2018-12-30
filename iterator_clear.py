from collections import Iterable,Iterator


class test(object):
    def __init__(self):
        #create empty list
        self.name=list()
        self.current_position=0

    def add(self,val): #receive
        #append some cuti cuti
        self.name.append(val)


    def __iter__(self):
        return  self

    def __next__(self):
        if self.current_position < len(self.name):
            #next like one time for
            item=self.name[self.current_position]
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
