def loop(arr):

    for i in range(0 , len(arr)):

        for j in range(0 , len(arr)):

            print(arr[i][j],end=" ")

        print()


arr = [[0 for _ in range(4)] for _ in range(4)]

loop(arr)

