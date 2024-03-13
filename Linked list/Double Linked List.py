class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class doublelinkedlist:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_ending(self, data):
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
            dll += str(itr.data) + '-->'
            itr = itr.next
        print(dll)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        # print(count)
        return count

    def get_lastnode(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def print_backward(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr = self.get_lastnode()
        dll = ''
        while itr:
            dll += str(itr.data) + "-->"
            itr = itr.prev
        print(dll)

    def insert_values(self, values):
        self.head = None

        for data in values:
            self.insert_ending(data)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("INvalid Index")

        if index == 0:
            self.insert_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node

            itr = itr.next
            count += 1



if __name__ == "__main__":
    dll = doublelinkedlist()
    dll.insert_ending(5)
    dll.insert_ending(15)
    dll.insert_ending(25)
    dll.insert_values(['Anand', 'Mahithra', 'Dora'])
    dll.print_backward()
    dll.print_forward()
    dll.insert_at(1 ,"Love")
    dll.print_forward()
    # dll.print_forward().