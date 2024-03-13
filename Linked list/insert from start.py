import math


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linkedlist:
    def __init__(self):
        self.head = None

    def insert_from_start(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        itr = self.head
        if itr is None:
            print("Linked list is empty")
            return

        lldata = ""
        while itr:
            lldata += str(itr.data) + "-->"
            itr = itr.next

        print(lldata)

    def insert_from_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data):
        self.head = None
        for i in data:
            self.insert_from_end(i)

    def get_count(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def remove_index(self, index):
        if index < 0 or index > self.get_count():
            raise Exception("Invalid index")

        itr = self.head
        if index == 0:
            # self.head = self.head.next
            self.head = self.head.next
            return


        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_at(self, index, data):
        if index<0 or index>self.get_count():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_from_start(data)

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if str(itr.data) == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        itr = self.head
        while itr:
            pre = itr
            if str(pre.data) == data:
                pre = pre.next
                break
            itr = itr.next

    def problem(self, k):
        ind = self.get_count()
        index = math.ceil(ind/k)
        itr = self.head
        a = 0
        while itr:
            if a == index-1:
                print(itr.data)
                break
            itr = itr.next
            a += 1


if __name__ == "__main__":
    ll = linkedlist()
    ll.insert_from_end(52)
    ll.insert_from_end(55)
    ll.insert_from_end(100)
    ll.insert_from_end(33)
    ll.problem(1)

    # ll.insert_from_end(1)52 55 100 33
    # 1
    # ll.insert_values(["A", "N", "A", "N", "D"])
    # ll.print()
    # ll.insert_after_value("D", "Mahi")
    # print("length of linked list: ", ll.get_count())
    # # ll.remove_index(4)
    # # ll.insert_at(5, "M")
    # ll.remove_by_value("D")
    ll.print()

