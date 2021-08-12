arr = input().split(',')

dic = {1:{}, 2:{}, 3:{}}

for pos in arr:
    for i in range(3):
        if( pos[i] not in dic[i+1] ):
            dic[i+1][pos[i]] = 1
        else:
            dic[i+1][pos[i]]+=1

res = ''

for key,val in dic.items():
    a,b='',0
    for k,v in val.items():
        if(v>b):
            a=k
    res+=a
    
print(res)
