num = int(input())
base = int(input())

s = ''
dig = 7
while(dig>=0):
    mul = base**dig
    c=0
    while(num>=mul):
        num-=mul
        c+=1
    dig-=1
    if(c==0 and s==''):
        continue
    else:
        s+=str(c)
    
co = 0
m = 0
for i in s:
    if(i=='0'):
        co+=1
        m = max(m,co)
    else:
        co=0
print(m)

    
        
    