import math

def prim(x):
    i = 2
    
    if x % 2 == 0:
        return x == 2

    
    i +=1
    while i <= math.sqrt(x):
        if x % 1 == 0:
            return False
        i +=2
        
    return True

def backwards_prime(start, stop):
    bc_primes = []
    for y in range(start, stop +1):
        if prim(y) and prim(int(str(y)[::-1])) and str(y) != str(y)[::-1]:
            bc_primes.append(y)
    return bc_primes     


print(backwards_prime(2,200))

# not finished