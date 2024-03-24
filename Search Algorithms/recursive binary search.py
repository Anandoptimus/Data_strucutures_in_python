def binary_search(number_list, number_to_find, left, right):
    if right < left:
        return -1

    mid_index = (left + right) // 2
    mid_number = number_list[mid_index]

    if mid_number == number_to_find:
        return mid_index
    elif mid_number < number_to_find:
        return binary_search(number_list, number_to_find, mid_index+1, right)
    else:
        return binary_search(number_list, number_to_find, left, mid_index-1)


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number_to_find = 1
left = 0
right = len(number_list)
linear_search = binary_search(number_list, number_to_find, left, right)
if linear_search == -1:
    print("number is not found in the list")
else:
    print(f"Number to be found is present in the index of {linear_search}")
