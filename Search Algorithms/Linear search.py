def LinearSearch(number_list, number_to_find):
    new_list = []
    for index, number in enumerate(number_list):
        if number == number_to_find:
            new_list.append(index)
    if new_list:
        return new_list
    return -1


number_list = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
number_to_find = 15
linear_search = LinearSearch(number_list, number_to_find)
if linear_search == -1:
    print("number is not found in the list")
else:
    print(f"Number to be found is present in the index of {linear_search}")
