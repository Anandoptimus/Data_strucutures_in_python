class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Double_linked_list:
    def __init__(self):
        self.head = None

    def insert_from_beginning(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
            return
        node = Node(data, self.head, None)
        self.head = node
        self.head.prev = node

    def insert_from_ending(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def print_forward(self):
        if self.head is None:
            print('linked list is empty')
            return
        itr = self.head
        dll = ''
        while itr:
            dll += str(itr.data) + "-->"
            itr = itr.next
        print(dll)

    def get_lastnode(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def print_backward(self):
        if self.head is None:
            print('linked list is empty')
            return
        itr = self.get_lastnode()
        dll = ''
        while itr:
            dll += str(itr.data) + '-->'
            itr = itr.prev
        print(dll)

    def get_length(self):
        itr = self.head
        count = 0

        while itr:
            count += 1
            itr = itr.next
        # print(count)
        return count

    def insert_values(self, values):
        for data in values:
            self.insert_from_ending(data)

    def insert_at(self, index, value):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_from_beginning(value)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(value, itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1


if __name__ == '__main__':
    dll = Double_linked_list()
    # dll.insert_from_beginning(5)
    # dll.insert_from_beginning(15)
    # dll.insert_from_beginning(25)
    # dll.insert_from_ending(5)
    # dll.insert_from_ending(15)
    # dll.insert_from_ending(25)
    dll.insert_values(['Anand', 'Mahu', 'Dora'])
    dll.print_forward()
    dll.print_backward()
    dll.insert_at(1, 'love')
    dll.print_forward()
    dll.remove_at(1)
    dll.print_forward()
    dll.get_length()
