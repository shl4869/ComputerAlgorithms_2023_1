
# Quick_Sort

def pivotSelect(arr, low, high, tcom):
    pivot = low
    if tcom == 1:
        # Time Complexity n^2
        # Select pivot as the max value
        for i in range(low,high+1):
            if arr[pivot] < arr[i]:
                pivot=i
    elif tcom == 2:
        # Time Complexity n(log n)
        # Select pivot as the median value
        for i in range(low+1,high,2):
            if (arr[i] <= arr[i+1] <= arr[pivot]) or (arr[pivot] <= arr[i+1] <= arr[i]):
                pivot = i+1
            elif (arr[i+1] <= arr[i] <= arr[pivot]) or (arr[pivot] <= arr[i] <= arr[i+1]):
                pivot = i
    else:
        print("pivot select error")
    # return the selected pivot
    print("p_index:",pivot,"\tpivot: ",arr[pivot])
    return pivot

def partition(arr,low,high,tcom):
    # choose the pivot
    p_index=pivotSelect(arr,low,high,tcom)
    (arr[p_index],arr[high])=(arr[high],arr[p_index])
    pivot=arr[high]
    i = low-1
    
    # compare each element with pivot
    for j in range(low,high):
        if arr[j]<=pivot:
            i += 1
            (arr[i],arr[j])= (arr[j],arr[i])
            print(i,j,arr)
    (arr[i+1],arr[high])=(arr[high],arr[i+1])
    print(i,j,arr)

    # return the position where partition is done
    return i+1

def quickSort(arr,low,high,tcom):
    if low<high:
        # Find pivot element
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        c_pivot = partition(arr,low,high,tcom)
        # recursive call on the left array of pivot
        quickSort(arr,low,c_pivot-1,tcom)
        # recursive call on the right array of pivot
        quickSort(arr,c_pivot+1,high,tcom)

if __name__=="__main__":
    array1 = [21,3,12,15,7,32,4,25,9,18]
    print("***pivot: MAX***\nOriginal Array: ", array1)
    quickSort(array1,0,len(array1)-1,1)
    print ("\nSort Result: ", array1)

    array2 = [21,3,12,15,7,32,4,25,9,18]
    print("\n***pivot: MID***\nOriginal Array: ", array2)
    quickSort(array2,0,len(array2)-1,2)
    print ("\nSort Result: ", array2)
