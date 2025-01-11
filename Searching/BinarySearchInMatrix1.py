''''
This is the Binary Search in Matrix Pattern 1 by  kunal kushwaha . Time complexity is : O(log mn )
'''

def binary(arr):

    n = len(arr)

    target = int(input("Enter the target element : "))

    s = 0
    e = len(arr[0])-1

    while s <= n-1 and e >= 0 :

        if target < arr[s][e]:

            e -= 1

        elif target > arr[s][e]:

            s += 1

        else :
            result = [
                [s],[e]
            ]
            return result

    result = [
        [-1],[-1]
    ]
    return result

arr = [
    [10,20,30,40],
    [11,22,33,44],
    [13,23,34,45],
    [17,27,37,47]
]

result = binary(arr)

if result[0][0] == -1 and result[1][0] == -1 :
    print("Element Not found !")
else :
    print(f"So the row index of the target element is : {result[0][0]} and column index of the target element is : {result[1][0]}")