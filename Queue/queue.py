from collections import deque




class Queue:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.appendleft(val)

    def pop(self):
        self.container.pop()

    def isempty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


if __name__ == '__main__':
    queue = Queue()
    queue.push(5)
    queue.push(15)
    queue.push(25)
    print(queue.container)
    print(queue.size())
    print(queue.isempty())
    queue.pop()
    print(queue.container)

