''''
Algorithm by Kunal kushwaha , Time complexity : O(log N) and Space Complexity : O(1)
'''

def quickSort(arr , low , high):

    if low >= high:

        return

    else :

        mid = low + (high - low )//2
        pivot = arr[mid]

        s = low

        e = high

    while s <= e:

        if arr[s] < pivot:

            s+=1
        if  arr[e] > pivot :

            e -= 1

        if s <= e :

            temp = arr[s]
            arr[s] = arr[e]
            arr[e] = temp

            s +=1
            e-=1

    quickSort(arr,low , e)
    quickSort(arr,s ,high)



arr = [5,4,3,2,1,5,2,0]

quickSort(arr , 0 , len(arr)-1)

print(arr)