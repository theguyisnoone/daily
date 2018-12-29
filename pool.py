from multiprocessing import Pool
import time
import os
import random

def test1(msg):#msg mains i
    start_time=time.time()#now time
    print('{}:start, pid:{}'.format(msg,os.getpid(),start_time))
    time.sleep(random.random()*3)
    end_time=time.time()
    print('{}:end ,pid:{},spend time:{}'.format(msg,os.getpid(),end_time-start_time))




po=Pool(3)#create pool num=3
for i in  range(10):
    po.apply_async(test1,(i,))#(i,) like args

print('start')

po.close()#close pool dont let more mission start
po.join()#let main process wait until other guys stop  dont same as threading
print('end')


# start
# 0:start, pid:712
# 1:start, pid:713
# 2:start, pid:714
# 2:end ,pid:714,spend time:1.2418708801269531
# 3:start, pid:714
# 0:end ,pid:712,spend time:1.4600040912628174
# 4:start, pid:712
# 1:end ,pid:713,spend time:1.9617390632629395
# 5:start, pid:713
# 3:end ,pid:714,spend time:0.7394180297851562
# 6:start, pid:714
# 6:end ,pid:714,spend time:0.1377112865447998
# 7:start, pid:714
# 4:end ,pid:712,spend time:2.0010430812835693
# 8:start, pid:712
# 5:end ,pid:713,spend time:2.0256168842315674
# 9:start, pid:713
# 9:end ,pid:713,spend time:0.1856849193572998
# 7:end ,pid:714,spend time:2.3309099674224854
# 8:end ,pid:712,spend time:2.7304930686950684
# end
