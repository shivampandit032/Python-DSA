from logging import setLoggerClass


def selection(arr , i , n):

    if i > n-2 :

        return

    max = 0
    for j in range(0 , n-i ):

        if arr[max] < arr[j]:

            max = j

    temp = arr[max]

    arr[max] = arr[n-i-1]

    arr[n-i-1] = temp

    return selection(arr , i+1 , n)


arr = [5,4,3,2,1]

selection(arr , 0 , len(arr))
print(arr)