def sol(n):
    if(int(n)//10):
        n2 = sum([int(i) for i in n])
        return sol(str(n2))
    else:
        return n

def superDigit(n, k):
    n2 = sum([int(i) for i in n])
    n2 = n2*k
    return sol(str(n2))
