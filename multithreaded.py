import threading, time
from queue import Queue


def fact(arr, q):
    print("working")
    result = 1
    for i in arr:
        result *= i
    q.put(result)


def fact1(arr, q):
    print("working")
    result = 1
    for i in arr:
        result *= i
    q.put(result)


if __name__ == "__main__":
    q = Queue()
    num = int(input("enter number"))
    t1 = time.time()
    numbers = range(1, num)
    parts = [numbers[i::2] for i in range(2)]
    th = threading.Thread(target=fact, args=(parts[0], q))
    th.start()
    th1 = threading.Thread(target=fact1, args=(parts[1], q))
    th1.start()
    th.join()
    th1.join()

    result = 1
    for c in range(0, 2):
        result *= q.get()
    print(result)
    print("time: " + str((time.time() - t1)))
