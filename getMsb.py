def msbp(num):
    if num==0:
        return 0
    ones=1
    while num>>ones:
        ones+=1
    return ones


print(msbp(11))



#chnaging the number

def getMSB(n):
    if n==0:
        return 0
    msb=0
    #
    while(n!=0):
        n=n>>1
        msb+=1
    return msb   #it returns the index of the msb 
print(getMSB(11))