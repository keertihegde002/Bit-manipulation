# this function is used to get the sum of power of 2s in number


def sumofpow(n):
    res=[]
    for i in range(32):
        if n&(1<<i):
            res[i]=1   