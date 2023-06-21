
# Find minimum number of US postage stamps_Greedy Algorithm

def getStampQuantity(p_stamp,cost):
    q_stamp = [0]*len(p_stamp)
    s_stamp=0
    # get the maximum number of stamp that fit the cost for each stamp
    # update the cost with the remainder
    # after paying with the maximum number of stamp
    # check from most expensive one to cheapest one
    for i in range(len(p_stamp)-1,-1,-1):
        q_stamp[i]=cost//p_stamp[i]
        cost%=p_stamp[i]
        s_stamp+=q_stamp[i]
        #print(p_stamp[i],"cent post:",q_stamp[i],"\tcost: ",cost)
    print("Cost of stamp = ",p_stamp)
    print("Quantity of stamp = ",q_stamp)
    print("total stamp: ",s_stamp)

if __name__=="__main__":
    p_stamp=[1,10,21,34,70,100,350,1225,1500]
    cost = 140
    getStampQuantity(p_stamp,cost)
