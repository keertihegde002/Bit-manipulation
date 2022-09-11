def reverseBits(n):
    rev=0
    for i in range(32): # since we have 32 bits in integer 
        bit=(n>>i)&1         #this will check if the number at i is set or unset
                         #another way would be , if you dont want to dchange n
                         # n&(1<<i)
        rev=rev|(bit<<(31-i)) #as we need to sdtore the lsb at msb