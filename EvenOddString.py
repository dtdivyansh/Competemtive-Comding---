s = input()
even = []
odd = []

c = 0

for i in s:
    if( i.isnumeric() ):
        n = int(i)
        if(n&1):
            odd.append(n)
        else:
            even.append(n)
    elif(i.isalpha()):
        continue
    else:
        c+=1
        
print(even,odd)
if(c&1):
    even2 = even.copy()
    even  = odd.copy()
    odd = even2
    
res = ''
print(even,odd)
while(odd or even):
    if(even):
        res = res + str(even.pop(0))
    if(odd):
        res = res + str(odd.pop(0))

print(res)   
    