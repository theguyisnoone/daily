'''something about enumerate()'''

names=['a','b','c']

for temp in names:
    print(temp)

#a
#b
#c

print('>>>')
for temp in enumerate(names):

    print(temp)


# (0, 'a')
# (1, 'b')
# (2, 'c')

print('>>>unpack')
for i,temp in enumerate(names):
    print(temp)
