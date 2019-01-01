def fibonacci(all_len):
    current_position=0
    a, b=0, 1

    while current_position < all_len:
        yield a #!!!
        a ,b=b, a+b
        current_position +=1
    return 'ok'


obj=fibonacci(10)#like a  class

#something about next...
while True:
    try:
        ret=next(obj)
        print(ret)
    # except StopIteration
    except Exception as ret:
        print(ret.value)
        break







#1.create serval objections
#doesnt disturb each other

# obj2=fibonacci(2)
#
# for i in obj:
#     print('obj',i)
#
# for i in obj2:
#     print('obj2',i)
