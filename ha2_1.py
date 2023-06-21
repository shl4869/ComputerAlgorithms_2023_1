def lis(arr):
    n=len(arr)
    # h_i values for all indexes
    h=[1]*n
    # preceeding element for lis
    pre=[-1]*n
    # update preceeding element and lis
    # when meeting element smaller than present element
    # and its lis length+1 is bigger than present lis length
    for i in range(1,n):
        for j in range(0,i):
            if arr[i]>arr[j] and h[i] < h[j] + 1:
                h[i] = h[j]+1
                pre[i]=j
    # get the maximum length lis and the biggest element for lis
    max_len = 0
    for i in range (n):
        if (max_len<h[i]):
            max_len=h[i]
            max_val=i
    # get LIS array by visiting preceeding elements in lis
    lis=[0]*max_len
    lis[max_len-1]=arr[max_val]
    k = max_val
    pos = max_len-2
    while (k>0):
        lis[pos]=arr[pre[k]]
        k=pre[k]
        pos-=1
    # print lis and the length of the lis
    print("LIS: ",lis)
    return max_len

if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print("Length of lis is",lis(arr))
