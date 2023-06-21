# global variable to count the number of comparison
# for each finding algorithm 
global comparisonAlgo1
global comparisonAlgo2
comparisonAlgo1 = 0
comparisonAlgo2 = 0

def MaxMin1(A):
    # use global variable to keep track of the count of comparison
    global comparisonAlgo1
    # initialize min and max as the first element of the array
    maxNum = A[0]
    minNum = A[0]

    # compare all element with current min, max
    # and update if the element is smaller than min or bigger than max
    for i in range(1,len(A)):
        comparisonAlgo1+=2
        if maxNum < A[i]:
            maxNum = A[i]
        if minNum > A[i]:
            minNum = A[i]
    return minNum, maxNum

def MaxMin2(A,i,j):
    # use global variable to keep track of the count of comparison
    global comparisonAlgo2

    # when there is one element, max and min is both the element
    # no comparison needed
    if i==j:
        return A[i], A[i]
    # when there is two elements, max is bigger element and min is smaller element
    # one comparison needed
    elif (j-i) == 1:
        if A[i]<A[j]:
            comparisonAlgo2+=1
            return A[i],A[j]
        else:
            comparisonAlgo2+=1
            return A[j],A[i]
    # when there is two or more elements, divide the array in to two arrays
    # and get min and max for each subarray
    # then, compare two mins and maxes to get the min and max for this level
    # 2(n/2)+2 comparisons needed
    else:
        minLeft , maxLeft = MaxMin2(A,i,(i+j)//2)
        minRight, maxRight = MaxMin2(A,(i+j)//2+1,j)
        comparisonAlgo2+=2
        return (min(minLeft,minRight), max(maxLeft,maxRight))
    
if __name__ == '__main__':
    A = [24, 75, 92, 83, 61, 48, 97, 50]
    
    print("Original Array: ",A)
    print("Length of Array: ",len(A))

    # First Algorithm
    # number of comparison: 2n-2
    print("\nMinMax1(): ")
    print("result: ",MaxMin1(A))
    print("# of comparison: ",comparisonAlgo1)
    # Second Algorithm
    # number of comparison: 3/2n-2
    print("\nMinMax2(): ")
    print("result: ",MaxMin2(A,0,len(A)-1))
    print("# of comparison: ",comparisonAlgo2)
    
