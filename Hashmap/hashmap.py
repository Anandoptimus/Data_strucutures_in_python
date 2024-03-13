class hashtable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def __gethash__(self, item):
        h = 0
        for i in item:
            h += ord(i)
        return h % self.MAX

    def __getitem__(self, item):
        h = self.__gethash__(item)
        for element in self.arr[h]:
            if element[0] == item:
                return element[1]

    def __setitem__(self, key, value):
        h = self.__gethash__(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                found = True
                self.arr[h][index] = (key, value)
                break
        if not found:
            self.arr[h].append((key, value))

    def __delitem__(self, key):
        h = self.__gethash__(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
        # self.arr[h] = None


hm = hashtable()
# print(hm.__gethash__('march 6'))
# print(hm.__gethash__('march 17'))
# print(hm.__gethash__('march 26'))

print(hm.arr)
hm['march'] = 15
hm['march1'] = 15
hm['march2'] = 15
hm['march3'] = 15
hm['march 17'] = 20
print(hm.__getitem__('march 17'))
print(hm.arr)
del hm['march 17']
print(hm.arr)