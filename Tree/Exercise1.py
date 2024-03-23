class Tree:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination
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

    def print(self, property):
        if property == "both":
            value = self.name + ' (' + self.destination + ')'
        elif property == 'name':
            value = self.name
        else:
            value = self.destination

        space = " " * self.get_level() * 3
        prefix = space + '|__' if self.parent else ""
        print(prefix + value + " " +str(self.get_level()))
        if self.children:
            for child in self.children:
                child.print(property)
                # print(child.get_level())


def exercise1():
    root = Tree('Nilupul', 'CEO')

    Chinmay = Tree('Chinmay', 'CTO')

    Vishwa = Tree('Vishwa', 'Infrastructure Head')
    Vishwa.add_child(Tree('Dhaval', 'Cloud Manager'))
    Vishwa.add_child(Tree('Abhijit', 'App Manager'))

    Chinmay.add_child(Vishwa)
    Chinmay.add_child(Tree('Aamir', 'Application Head'))

    Gels = Tree('Gels', 'HR Head')
    Gels.add_child(Tree('Peter', 'Recruitment Manager'))
    Gels.add_child(Tree('Wagas', 'Policy Manager'))

    root.add_child(Chinmay)
    root.add_child(Gels)

    root.print('both')
    print()
    root.print('name')
    print()
    root.print('mahi')

if __name__ == '__main__':
    exercise1()


