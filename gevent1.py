import gevent

'''create three obj each obj have 5 eggs
   one obj finished one obj continue
'''
def f(n):
    for i in range(n):
        print(gevent.getcurrent(),i)

g1=gevent.spawn(f,5)
g2=gevent.spawn(f,5)
g3=gevent.spawn(f,5)
g1.join()
g2.join()
g3.join()



# <Greenlet "Greenlet-0" at 0x10e7cd148: f(5)> 0
# <Greenlet "Greenlet-0" at 0x10e7cd148: f(5)> 1
# <Greenlet "Greenlet-0" at 0x10e7cd148: f(5)> 2
# <Greenlet "Greenlet-0" at 0x10e7cd148: f(5)> 3
# <Greenlet "Greenlet-0" at 0x10e7cd148: f(5)> 4

# <Greenlet "Greenlet-1" at 0x10e7cd248: f(5)> 0
# <Greenlet "Greenlet-1" at 0x10e7cd248: f(5)> 1
# <Greenlet "Greenlet-1" at 0x10e7cd248: f(5)> 2
# <Greenlet "Greenlet-1" at 0x10e7cd248: f(5)> 3
# <Greenlet "Greenlet-1" at 0x10e7cd248: f(5)> 4

# <Greenlet "Greenlet-2" at 0x10e7cd348: f(5)> 0
# <Greenlet "Greenlet-2" at 0x10e7cd348: f(5)> 1
# <Greenlet "Greenlet-2" at 0x10e7cd348: f(5)> 2
# <Greenlet "Greenlet-2" at 0x10e7cd348: f(5)> 3
# <Greenlet "Greenlet-2" at 0x10e7cd348: f(5)> 4
