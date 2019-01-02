def fibonacci(all_len):
    current_position=0
    a, b=0, 1

    while current_position < all_len:
        ret=yield a #!!!
        print('>>>ret>>>',ret)
        a ,b=b, a+b
        current_position +=1
    return 'ok'


obj=fibonacci(10)#like a  class


ret=next(obj)
print(ret)

#or
# ret=obj.send(None)
# print(next)




ret=obj.send('hahah')
print(ret)

ret=obj.send('ah')
print(ret)

ret=obj.send('ddah')
print(ret)


'''>>>print'''
# 0
# >>>ret>>> hahah
# 1
# >>>ret>>> ah
# 1
# >>>ret>>> ddah
# 2
