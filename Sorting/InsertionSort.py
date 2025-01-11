''''
This is One of the Sorting Algorithm .
Time complexity of the Algorithm is : O(N**2 ) and Space Complexity is : O(1)
'''

def insertion(arr):

    n = len(arr)

    for  i in range(0, n-1):

        for  j in range(i+1 , 0 , -1):

            if arr[j] < arr[j-1]:

                temp = arr[j]

                arr[j] = arr[j-1]
                arr[j-1] = temp

arr = [5,4,2,3,1]

insertion(arr)

print(arr)
