''''
This is One of the Sorting Algorithm . This Algorithm is Use to sort for input where input sequence is " 1 to N [1,N] " or " 0 to N [0,N] "
Time complexity of the Algorithm is : O(N) and Space Complexity is  : O(1 )
'''

def cycle(arr):
    n = len(arr)

    for i in range(0 , n):

        correctIndex = arr[i]-1

        if arr[correctIndex] != arr[i]:

            temp = arr[correctIndex]

            arr[correctIndex] = arr[i]

            arr[i] = temp

arr = [5,4,3,2,1]

cycle(arr)

print(arr)