'''
This is the sorting algorithm by Take u forward , Time complexity  : O(log N)  and Space complexity : O(n)
'''
def merge(arr  , low , high ) :

    if low >= high :

        return

    else :
        mid = (low + high)//2
        merge(arr , low , mid )
        merge(arr , mid + 1 , high)

        mergeSort(arr , low , mid , high)

        return

def mergeSort(arr , low , mid , high):

            result = []
            s = low
            e = mid + 1

            while s <= mid and e <= high:

                if arr[s] <= arr[e]:

                    result.append(arr[s])

                    s+=1

                else :

                    result.append(arr[e])
                    e+=1

            while s<=mid:

                result.append(arr[s])
                s+=1
            while e <= high:

                result.append(arr[e])
                e+=1

            for i in range(low , high+1):

                arr[i] = result[i-low]

            return

arr = [5,4,3,2,1,0]

merge(arr,0,len(arr)-1)

print(arr)