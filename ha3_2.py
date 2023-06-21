# ComputerAlgorithms 2071035 Lee Somin
# HA 3-2: Subset Sum

M = 9 # Value of subset sum wanted
w = [3, 34, 4, 12, 5, 2] # array which to find the subset sum from

def sum_of_subsets(i,wsum,rsum,nodes,W):
    #check whether to keep expanding
    if((wsum+rsum>=M) and ((wsum == M) or (wsum+W[i+1]<=M))):
        # when subset sum equals to M is found,
        # print the solution
        if(wsum == M):
            print(nodes)
        else:
            # select i+1th int and check if
            nodes.append(W[i+1])
            # update wsum, rsum and call sum_of_subset for child nodes
            # to check if child nodes meet the subset sum condition
            sum_of_subsets(i+1,wsum+W[i+1],rsum-W[i+1],nodes,W) 
            # deselect(i+1th int) 
            nodes.pop()
            # update wsum, rsum and call sum_of_subset for child nodes
            # to check if child nodes meet the subset sum condition
            sum_of_subsets(i+1,wsum,rsum-W[i+1],nodes,W)


if __name__=='__main__':
    nodes=[] # array of elements added for subset sum
    rsum=0 # sum of remaining values in original array
    # sort w in to W which is in ascending order
    W = sorted(w)
    # add all elements of original array to initialize rsum
    for i in w:
        rsum+=i
    # find subset that satisfies the condition
    print("***SOLUTION***")
    # start from node 0, and the function will call sum_of_subsets(0 ~ )
    sum_of_subsets(-1,0,rsum,nodes,W)
    
