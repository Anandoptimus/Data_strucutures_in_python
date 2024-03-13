from collections import deque
import threading
import time


class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, val):
        self.container.appendleft(val)

    def dequeue(self):
        if self.size() == 0:
            print('queue is empty')
            return
        return self.container.pop()

    def isempty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def front(self):
        return self.container[-1]


queue = Queue()

def place_order(val):
    for i in val:
        print("Placing order is ", i)
        queue.enqueue(i)
        time.sleep(0.5)


def serve_order():
    time.sleep(1)
    while True:
        order = queue.dequeue()
        if order == None:
            break
        print("Now serving: ", order)
        time.sleep(2)

def binary_number(n):
    queue = Queue()
    queue.enqueue('1')

    for i in range(n):
        front = queue.front()
        print(' ', front)
        queue.enqueue(front+ "0")
        queue.enqueue(front+ "1")

        queue.dequeue()


if __name__ == '__main__':
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    t1 = threading.Thread(target=place_order, args=(orders, ))
    t2 = threading.Thread(target=serve_order )

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # Exercise 2
    binary_number(10)




