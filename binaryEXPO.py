from re import A


def binaryExpo(base,power):
    res=0
    while power>0:
        if power&1:
            res*=base
        a*=a 
        power>>=1
    return res