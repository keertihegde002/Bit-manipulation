


def countSetBit(n):
    """ 
    s=str(bin(n))[2:]  we are slicing by two , as bin return 0b101 for n=5
    return s.count("1)  this will take o(n)
    """
    #optimised way
    ct=0
    while n:
        ct+=1
        n=n&(n-1)
    return ct

def getBinary(n):
    return str(bin(n))[2:]


def binToInteger(n):
    return int(n,2)

#kth bit set or not  

def Kthbit(n,k):
    t=n&(1<<(k-1))  # k-1 if we consider lsb index as 1 , k if we take lsb index as 0
    if t:
        return True
    return False
print(Kthbit(5,1))