A = [i for i in input().split(',')]
B = [i for i in input().split(',')]
C = [i for i in input().split(',')]
D = [i for i in input().split(',')]

cars = int(input())

la = len(A)
lb = len(B)
lc = len(C)
ld = len(D)

a = 10 - la
b = 10 - lb
c = 10 - lc
d = 10 - ld

start = [la,lb,lc,ld]

free = [a,b,c,d]

ans = []

alpha = 'ABCD'
while(cars>0):
    m = max(free)
    ind = free.index(m)
    char =   alpha[ind]
    while(m>0):
        m-=1
        cars-=1
        free[ind]-=1
        start[ind]+=1
        temp = char+str(start[ind])
        ans.append(temp)
        if(cars==0):
            break

print(ans)

'''
1,2,3,4

1,2,3

1,2

1,2,3,4,5

10
'''