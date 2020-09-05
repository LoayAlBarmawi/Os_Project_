import threading, time
from queue import Queue


def fact(arr,q):
    result = 1
    for i in arr:
        result *= i
    q.put(result)


if __name__ == "__main__":
    q=Queue()
    num = int(input("enter number"))
    t1 = time.time()
    numbers = range(1, num)
    parts = [numbers[i::1] for i in range(1)]
    th = threading.Thread(target=fact, args=(parts[0],q))
    th.start()



    result = 1

    result *= q.get()
    print(result)
    print("time: " + str((time.time() - t1)))
