class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_ending(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print('Linked List is empty')
        itr = self.head
        ll = ""
        while itr:
            ll += str(itr.data) + "-->"
            itr = itr.next
        print(ll)

    def get_count(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_values(self, values):
        for data in values:
            self.insert_at_ending(data)

    def remove_index(self, index):
        if index < 0 or index > self.get_count():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_by_index(self, index, data):
        if index < 0 or index > self.get_count():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_by_values(self, data, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_values(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if data == itr.next.data:
                itr.next = itr.next.next
                break
            itr = itr.next



if __name__ == "__main__":
    ll = linkedlist()
    # ll2 = linkedlist()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(15)
    # ll.insert_at_beginning(25)
    # ll2.insert_at_ending(5)
    # ll2.insert_at_ending(15)
    # ll2.insert_at_ending(25)
    # ll.get_count()
    # ll2.get_count()
    ll.insert_values(['Anand', 'mahi', 'Dora'])
    ll.print()
    # ll.remove_index(0)
    ll.insert_by_index(1, "Mahithra")
    ll.print()
    ll.insert_by_values("Anand", "Love")
    ll.print()
    ll.remove_by_values('mahi')
    ll.print()

    # ll2.print()

