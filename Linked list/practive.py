arr = [10, 20, 35, 50, 75, 80]
x = 70
for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            continue
        if arr[i] + arr[j] == x:
            print(i, j)
            break
        if arr[i] + arr[j] > x:
            break


