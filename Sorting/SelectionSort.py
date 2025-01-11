''''
This is One of the Sorting Algorithm , This is Unstable Sorting Algorithm .
Time complexity of the Algorithm is : O(N**2) and Space Complexity is : O(1)
'''

def selection(arr):

    n = len(arr)

    for i in range(0 , n-1):
        max = 0
        for j in range(0 , n-i):
            if arr[max] < arr[j]:

                max = j

        temp = arr[max]

        arr[max] = arr[n-i-1]

        arr[n-i-1] = temp

arr = [5,4,3,2,1]

selection(arr)

print(arr)
