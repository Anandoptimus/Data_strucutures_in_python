class Hashmap:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for _ in range(self.MAX)]

    def __gethash__(self, item):
        count = 0
        # print(f"here {item[0]}")
        for i in item:
            count += ord(i)
        # print(count)
        return count % self.MAX

    def __setitem__(self, item):
        # print(item[0])
        h = self.__gethash__(item[0])
        # print(h)
        found = True
        # update process
        for ind, ele in enumerate(self.arr[h]):
            if len(ele) == 2 and ele[0] == item[0]:
                # print('hi')
                self.arr[h][ind] = item
                found = False
                break
        if found:
            # print('hi')
            self.arr[h].append(item)

    def __getitem__(self, item):
        h = self.__gethash__(item)
        for i in self.arr[h]:
            if i[0] == item:
                print(i[1])
                return i[1]

    # def __getitem__(self, item):


def exercise2():
    with open('poem.txt', 'r') as file:
        fil = file.read()
        space_list = fil.split('\n')
        comma_list = []
        for i in space_list:
            comma_list.append(i.split(" "))
        poem = []
        for i in comma_list:
            for j in i:
                poem.append(j)
        # print(poem)
        dic = {}
        for i in poem:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        print(f"diverged: ", dic['diverged'],)
        print(f"in: ", dic['in'],)
        print(f"I: ", dic['I'])




def exercise1():
    with open('nyc_weather.csv', 'r') as file:
        fil = file.read()
        data = fil.split('\n')
        data.pop(0)
        print(data)
        month = []
        temp = []
        details = {}

        for i in data:
            month.append(i.split(",")[0])
            temp.append(i.split(",")[1])

        for i in range(len(month)):
            details[month[i]] = temp[i]

        print(details)

        temps = details.values()
        print(temps)
        avg = 0
        for i in temp:
            avg += int(i)
        print(f'The averge temp is {avg // 7}')
        print(f"The maximum temp in first 10 days {max(details.values())}")
        print(details['Jan 9'])
        print(details['Jan 4'])

        # print(final_data)
        # hash = Hashmap()
        # for i in final_data:
        #     # print(i)
        #     hash.__setitem__(i)
        # print(hash.arr)

        # hash.__getitem__('Jan 10')

        # print(final_data)
        # print(final_data[3])
        # print(hash.__gethash__(final_data[3]))

if __name__ == '__main__':
    exercise2()
