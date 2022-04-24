def power2(a,b):
    """ Computes a**b using iterated squaring
    Assume a,b are integers, b>=0 """
    
    result = 1
    while b>0: # b has more digits
        if b%2 == 1: # b is odd
            result = result*a
        a = a*a
        b = b//2 # discard b’s LSB
    return result

print(power2(5, 4))
