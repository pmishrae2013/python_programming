# Parity of a number refers to whether it contains an odd or even number of 1-bits. 
# The number has “odd parity”, if it contains odd number of 1-bits and is “even parity” if it contains even number of 1-bits.

def parity(x):
    result = 0
    while x:
        result ^= x & 1 #First "AND" operation of x & 1, then "XOR" operation with the earlier 'result'
        x>>=1
    return result


if __name__== '__main__':
    print(parity(11))

# XOR operation
# 1^1=0
# 0^0=0
# 1^0=1
# 0^1=1