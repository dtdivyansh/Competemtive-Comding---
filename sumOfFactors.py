def sumFactors(n):
    c = [n]
    for i in range(1,n//2+1):
        if(n%i==0):
            c.append(i)
    #print(c)
    return sum(c)

arr = [int(i) for i in input().split()]

res = []

for n in arr:
    if( sumFactors(n) in arr ):
        res.append(n)
if(res):
    print(res)
else:
    print(-1)