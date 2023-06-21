
# Improved in-place merge sort algorithm

def findMax(arr,start,end):
    # Find and return the max value in array
    max=0
    for k in range(start,end+1):
        if arr[k]>max:
            max=arr[k]
    return max

def merge(arr,start,mid,end):
    # Set key as the number that is greater than the max value of the array
    key=findMax(arr,start,end)+1
    # index is the position which merge data goes in to
    # start1, start2 are the positions where two arrays start
    index=start
    start1=start
    start2 = mid +1

    # If first element of second array is greater than the last element of
    # first array, the array is already sorted. return sorted array.
    if(arr[mid]<= arr[start2]):
        return

    # Check the data from two sorted array and merge until data of both arrays
    # are merged in to result array
    # Multiply the key and add the value to merge datum to the array
    # This key is used to save data on top of original array
    while (start1 <=mid or start2<=end):
        # When one array has merged all elements to the result array,
        # Put another array's leftover to the result array
        if(start1 > mid):
            arr[index]+= key*(arr[start2]%key)
            start2 += 1
            
        elif(start2 > end):
            arr[index]+=arr[start1]%key*key
            start1 += 1

        # Merge smaller element between the first element of two arrays
        # that hasn't been merged yet and shift the start point of source array
        elif(arr[start1]%key<=arr[start2]%key):
            arr[index]+= key*(arr[start1]%key)
            start1 += 1
            
        else:
            arr[index]+= key*(arr[start2]%key)
            start2 += 1
        # Increase index after merging one element to result array
        index+=1

    # Get Quotients of data divided by the key to get the sorted array of original data
    for i in range(start,end+1):
        arr[i]//=key
            
    

def mergeSort(arr,l,r):
    if(l<r):
        m=l+(r-l)//2
        # Sort fist and second halves
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        # Merge the sorted half-arrays
        merge(arr,l,m,r)

if __name__=='__main__':
    arr=[27, 10, 12, 20, 25, 13, 15, 22]
    mergeSort(arr,0,len(arr)-1)
    print("sorted array:",arr)


