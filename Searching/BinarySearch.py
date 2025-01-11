''''
Time Complexity of the Binary Search in 1D array Algorithm is : O(log N) .
'''
def binary(arr):
    n = len(arr)

    target = int(input("Enter the target element : "))

    s = 0
    e = n-1

    while s <= e:
        mid = s + (e - s)//2

        if target < arr[mid]:

            e = mid - 1

        elif target > arr[mid ]:

            s = mid + 1

        else :

            return mid

    return -1

arr = [1,2,3,4,5,6,7,8,9]

index = binary(arr)

if index == -1 :
    print("Element Not found !")
else :
    print(f"The index of the target element in the given array is : {index}")