#step 1
# def fibonacci(all_len):
#     current_position=0
#     a, b=0, 1
#     while current_position < all_len:
#         print(a)
#         a ,b=b, a+b
#         current_position +=1
#
# fibonacci(10)


#step2 become a  generator
# def fibonacci(all_len):
#     current_position=0
#     a, b=0, 1
#
#     while current_position < all_len:
#
#         yield a #!!!
#
#         a ,b=b, a+b
#         current_position +=1
#
#
# obj=fibonacci(10)#like a  class
# for i in obj:
#     print(i)



#step3 sequence
def fibonacci(all_len):
    current_position=0
    a, b=0, 1
    print('---1---')
    while current_position < all_len:
        print('---2---')
        yield a #!!!
        print('--3---')
        a ,b=b, a+b
        current_position +=1
        print('----4---')

obj=fibonacci(10)#like a  class
# for i in obj:
#     print(i)
ret=next(obj)#cause generator is a special Iterator
print(ret)
ret=next(obj)
print(ret)

''''>>>'''
# ---1---
# ---2---
# 0
# --3---
# ----4---
# ---2---
# 1
