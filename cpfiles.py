import os
from multiprocessing import Manager,Queue,Pool

#something about process

def copyfile(q,fname,origin_name,path):
    rfile=open(origin_name+'/'+fname,'rb')
    context=rfile.read()
    rfile.close()
    wfile=open(path+'/'+fname,'wb')
    wfile.write(context)
    wfile.close()
    print('over')

    q.put(fname)

def main():
    #origin folder name
    origin_name=input('请输入要复制的文件名的名字')
    path=input('复制的位置 绝对路径  复制在同路径下只要输入文件名')

    #new path include name #levelup
        #create backup file use os

    try:
        os.mkdir(path)
    except:
        pass

    #get  all filenames in origin folder
    fnames=os.listdir(origin_name)
    #create Pool
    po=Pool(3)
    #create queue
    q=Manager().Queue()
    #复制单位一个文件
    for fname in fnames:
        po.apply_async(copyfile,args=(q,fname,origin_name,path))
    #close pool
    po.close()
    alllen=len(fnames)
    while True:
        fname=q.get(fname)
        if fname in fnames:
            fnames.remove(fname)
            nowlen=len(fnames)
        copyrate=(alllen-nowlen)*100/alllen
        print('\rcopyrate:{}%'.format(copyrate))
        if copyrate == 100:
            break
    print()
    #print  finish rate
    po.join()

if  __name__ == '__main__':
    main()
