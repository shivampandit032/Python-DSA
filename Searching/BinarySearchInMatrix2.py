'''
This is the binary search in Matrix Pattern 2 , by Take U forward  . Time complexity is : O(log mn )
'''

def binary(arr):
    row = len(arr)
    col = len(arr[0])
    target = int(input("Enter the target element : "))
    s = 0
    e = (row * col)-1

    while s<= e:
        mid = s + (e-s)//2
        rI = mid // col
        cI = mid % col

        if target < arr[rI][cI]:
            e = mid -1

        elif target > arr[rI][cI]:

            s=mid + 1
        else :
            result  = [
                [rI],[cI]
            ]
            return result

    result = [
        [-1],[-1]
    ]
    return result

arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

result = binary(arr)

if result[0][0] == -1 and result[0][0] == -1 :
    print("Element Not found !")
else :
    print(f"So the row index of the target element is : {result[0][0]} and column index of the target element is : {result[1][0]}")