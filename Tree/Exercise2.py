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

    def print(self, level):
        if self.get_level() <= level:
            space = " " * self.get_level() * 3
            value = space + '|__' if self.parent else ""
            print(value + self.data + ' (Level: ' + str(self.get_level()) + ')')
        if self.children:
            for child in self.children:
                child.print(level)


class exercise2:
    def __init__(self):
        self.root = Tree('Global')

        india = Tree('India')
        usa = Tree('USA')

        Gujarat = Tree('Gujarat')
        Karnataka = Tree('Karnataka')

        Gujarat.add_child(Tree('Ahmedabad'))
        Gujarat.add_child(Tree('Baroda'))

        Karnataka.add_child(Tree('Bangaluru'))
        Karnataka.add_child(Tree('Mysore'))

        india.add_child(Gujarat)

        new_jersey = Tree("New Jersey")
        new_jersey.add_child(Tree('Princeton'))
        new_jersey.add_child(Tree('Trenton'))

        California = Tree('California')
        California.add_child(Tree('San Francisco'))
        California.add_child(Tree('Mountain View'))
        California.add_child(Tree('Palo Alto'))

        usa.add_child(new_jersey)
        usa.add_child(California)

        self.root.add_child(india)
        self.root.add_child(usa)

    def print_by_level(self, level):
        self.root.print(level)

if __name__ == "__main__":
    tree = exercise2()
    tree.print_by_level(0)
    print()
    tree.print_by_level(1)
    print()
    tree.print_by_level(2)
    print()
    tree.print_by_level(3)
