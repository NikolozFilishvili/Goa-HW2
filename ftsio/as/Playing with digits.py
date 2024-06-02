def dig_pow(n, p):
    summ = 0
    for c in str(n):
        summ+=int(c)**p
        p+=1
    if summ % n ==0:
        return summ / n
    else:
        return -1