class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return

        if data < self.data:
            # left node
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)

        else:
            # right node
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def inorder_traversal(self):
        element = []
        # left node
        if self.left:
            element += self.left.inorder_traversal()
        # base node
        element.append(self.data)
        # right node
        if self.right:
            element += self.right.inorder_traversal()

        return element

    def postorder_traversal(self):
        element = []
        # left node
        if self.left:
            element += self.left.postorder_traversal()
        # base node
        # right node
        if self.right:
            element += self.right.postorder_traversal()

        element.append(self.data)

        return element

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def preorder_traversal(self):
        element = []
        element.append(self.data)
        # left node
        if self.left:
            element += self.left.preorder_traversal()
        # base node

        # right node
        if self.right:
            element += self.right.preorder_traversal()

        return element

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculated_sum(self):
        left = self.left.calculated_sum() if self.left else 0
        right = self.right.calculated_sum() if self.right else 0
        return self.data + left + right

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.right is None and self.left is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

        return self


def build_tree(element):
    root = BinarySearchTree(element[0])
    for i in range(1, len(element)):
        root.add_child(element[i])

    return root


if __name__ == '__main__':
    numbers = [7, 4, 2, 1, 6, 11, 22, 344]
    values = build_tree(numbers)
    print(values.inorder_traversal())
    print(values.postorder_traversal())
    print(values.preorder_traversal())
    print(values.find_max())
    print(values.find_min())
    print(values.calculated_sum())
    print('does 1 is there: ', values.search(1))
    values.delete(344)
    print(values.inorder_traversal())
