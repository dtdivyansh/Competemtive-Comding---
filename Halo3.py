n = int(input())
if(n>12 or n<=2):
    print('INVALID BIRD')
else:
    birds = input().split()
    start = []
    for b in birds:
        l = len(b)
        if(l>5 or l<2 or ((b[0],b[-1]) in start)):
            print('INVALID BIRD')
            break
        start.append((b[0],b[-1]))                
    else:
        i=0
        c=n
        flag=1
        while(c>0):
            s = start[i][0]
            e = start[i][1]
            for j in range(n):
                if(start[j][0]==e and j!=i):
                     c-=1
                     i = j
                     break
            else:
                print('NO')
                break
        else:
            print('YES')
