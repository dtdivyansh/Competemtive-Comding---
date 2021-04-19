s = input()

dic = {}

for i in s:
    if( i.lower() not in dic.keys() ):
        dic[i.lower()] = [i]
    else:
        dic[i.lower()].append(i)
        
alpha = sorted( dic.keys() )

res = ''

n = len(alpha)

i = 0
j = n-1

while(i<j):
    res = res + ''.join(dic[alpha[i]]) + ''.join(dic[alpha[j]])
    i+=1
    j-=1
    
if(n&1):
    res = res + ''.join(dic[alpha[j]])
    
print(res)
    
    

