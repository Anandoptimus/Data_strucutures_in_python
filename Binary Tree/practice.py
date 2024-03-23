class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return

        elif data < self.data:
            if self.left:
                self.left.add_child(data)

            else:
                self.left = BinarySearchTree(data)

        elif data > self.data:
            if self.right:
                self.right.add_child(data)

            else:
                self.right = BinarySearchTree(data)

    def search(self, data):
        if self.data == data:
            return True

        elif data < self.data:
            if self.left:
                return self.left.search(data)

            else:
                return False

        elif data > self.data:
            if self.right:
                return self.right.search(data)

            else:
                return False

    def inorder_traversal(self):
        element = []
        if self.left:
            element += self.left.inorder_traversal()

        element.append(self.data)

        if self.right:
            element += self.right.inorder_traversal()

        return element

    def preorder_traversal(self):
        element = []
        element.append(self.data)
        if self.left:
            element += self.left.preorder_traversal()

        if self.right:
            element += self.right.preorder_traversal()

        return element

    def postorder_traversal(self):
        element = []
        if self.left:
            element += self.left.postorder_traversal()

        if self.right:
            element += self.right.postorder_traversal()

        element.append(self.data)
        return element

    def findmin(self):
        if self.left is None:
            return self.data
        return self.left.findmin()

    def findmax(self):
        if self.right is None:
            return self.data
        return self.right.findmax()

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

            max_val = self.left.findmax()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self


            # min_val = self.right.findmin()
            # self.data = min_val
            # self.right = self.right.delete(min_val)


def Build_tree(element):
    root = BinarySearchTree(element[0])
    for i in range(1, len(element)):
        root.add_child(element[i])

    return root


if __name__ == '__main__':
    numbers = [7, 4, 2, 1, 6, 11, 22, 344]
    root = Build_tree(numbers)
    print(root.inorder_traversal())
    print(root.preorder_traversal())
    print(root.postorder_traversal())
    print(root.calculated_sum())
    print(root.findmin())
    print(root.findmax())
    root.delete(344)
    print(root.inorder_traversal())
    print(root.preorder_traversal())


