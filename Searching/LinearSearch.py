def linear(arr):
    n = len(arr)
    target = int(input("Enter the target element : "))
    for i in range(0 , n,1):

        if  target == arr[i]:

            return i 

    return


arr = [1,2,3,4,5,6]

index = linear(arr)

if index == -1 :
    print("Element not found !")
else :
    print(f"So the index of the target element in the given array is : {index}")