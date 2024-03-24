def BinarySearch(number_list, number_to_find):
    left = 0
    right = len(number_list)
    mid = 0
    new_list = []
    while left <= right:
        mid = (left + right) // 2
        mid_number = number_list[mid]
        print(mid_number)
        if mid_number == number_to_find:
            new_list.append(mid)
        if mid_number < number_to_find:
            left = mid + 1
        else:
            right = mid - 1
    return new_list


number_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
number_list = sorted(number_list)
print(number_list)
number_to_find = 15
binary_search = BinarySearch(number_list, number_to_find)
if binary_search == -1:
    print("Number is not found in the list")
else:
    print(f"Number to be found is present in the index of {binary_search}")
