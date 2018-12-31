输入
这是迭代器
nums=[x*2 for x in range(10)]

-->
In [2]: nums
Out[2]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

把列表推导式的方括号换成了圆括号
生成器
-->
In [4]: nums=(x*2 for x in range(10))

In [5]: nums
Out[5]: <generator object <genexpr> at 0x10e68b7d8>

In [6]: for num in nums:
   ...:     print(num)
   ...:
0
2
4
6
8
10
12
14
16
18


函数加yield自动变成生成器
