# Find minimum number of US postage stamps_Dynamic Programing

import sys

def minStamp(p_stamp, q_stamp, cost):
    # store the minimum number of postage for i value.
    dp = [0]*(cost+1)
    # Base case (If given cost is 0)
    dp[0] = 0
    # initiate the number of total stamp for each cost as max
    for i in range(1,cost+1):
        dp[i] = sys.maxsize
    # find minimum number of stamp for each cost
    for i in range(1,cost+1): # all values up to cost
        for j in range (q_stamp): # all stamps in array
            if(p_stamp[j]<=i):
                sub_res = dp[i-p_stamp[j]] # subproblem result
                # if the result of subproblem+1 is smaller than
                # current number of stamp, update the number
                if (sub_res != sys.maxsize and sub_res +1 < dp[i]):
                    dp[i] = sub_res+1
    return dp[cost]

if __name__=='__main__':
    p_stamp=[1,10,21,34,70,100,350,1225,1500]
    q_stamp = len(p_stamp)
    cost = 140
    print("Minimum Stamp required is ",minStamp(p_stamp, q_stamp, cost))
