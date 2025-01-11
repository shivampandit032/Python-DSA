''''
This is One of the Sorting algorithm , This is "Stable Algorithm " .
Time complexity of the Algorithm is : O( N**2 ) and Space Complexity of the given algorithm is : O(1)
'''

def bubble(arr):
    n = len(arr)

    for i in range(0 , n-1):

        for j in range(1 , n-i):

            if arr[j] < arr[j-1]:

                temp = arr[j]

                arr[j] = arr[j-1]

                arr[j-1] = temp

arr = [5,4,3,2,1]
bubble(arr)

print(arr)