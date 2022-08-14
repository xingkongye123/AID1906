from multiprocessing import Queue,Process
from time import sleep
from random import randint
q=Queue(5)
def handle():
    a=[]
    while True:
        x=randint(1,33)
        if x not in a:
            a.append(x)
            q.put(x)
        if len(a)==6:
            break
    q.put(randint(1,16))
def request():
    l=[]
    for i in range(6):
        l.append(q.get())
    l.sort()#排序函数
    l.append(q.get())
    print(l)
p1 = Process(target=handle)
p2 = Process(target=request)
if __name__ == '__main__':
    p1.start()
    p2.start()
    p1.join()
    p2.join()
