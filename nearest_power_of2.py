def pow2(n):
    if n==1:
        return 0

    while n&(n-1)!=0:
        n=n&(n-1)
        
    return n

print(pow2(8))