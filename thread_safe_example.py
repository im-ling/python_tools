# 线程同步:
# 实例化一把锁 mutex = threading.Lock()
# 上锁 mutex.acquire()
# 释放锁 mutex.release()


import threading

# 定义全局变量
g_num = 0
# 实例化一把锁
mutex = threading.Lock()

def sum_num1():
    with mutex:
        for _ in range(1000000):
            global g_num
            g_num += 1
        print('sum1:', g_num)


def sum_num2():

    # 上锁
    mutex.acquire()

    for _ in range(1000000):
        global g_num
        g_num += 1

    print('sum2:', g_num)

    # 释放锁
    mutex.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=sum_num1)
    t2 = threading.Thread(target=sum_num2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('主进程:', g_num)

