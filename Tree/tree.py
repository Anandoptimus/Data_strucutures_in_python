class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        space = "  " * self.get_level() * 3
        prefix = space + "|-->" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product():
    root = Tree("Electronics")

    laptop = Tree("laptop")
    laptop.add_child(Tree('Mac'))
    laptop.add_child(Tree('Surface'))
    laptop.add_child(Tree("ThinkPad"))

    cellphone = Tree("cellphone")
    cellphone.add_child(Tree('iphone'))
    cellphone.add_child(Tree('Google pixel'))
    cellphone.add_child(Tree('Vivo'))

    tv = Tree('tv')
    tv.add_child(Tree('Samsung'))
    tv.add_child(Tree('LG'))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    cellphone.print_tree()

if __name__ == "__main__":
    build_product()