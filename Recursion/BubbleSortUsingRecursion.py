def bubble(arr, i, n):
    if i > n - 2:
        return

    for j in range(1 , n-i):

        if arr[j] < arr[j - 1]:
            temp = arr[j]

            arr[j] = arr[j - 1]

            arr[j - 1] = temp

    return bubble(arr , i+1 , n)

arr = [5,4,3,2,1]

bubble(arr , 0 , len(arr))

print(arr)