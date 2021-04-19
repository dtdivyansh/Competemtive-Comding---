s = input()

num = []

for i in s:
    if(i.isdigit()):
        num.append(int(i))

num = set(num)
num = list(num)

even = 10

for i in num:
    if(i%2==0 and i<even):
        even = i

num.remove(even)

num.sort(reverse=True)

res = ''

for i in num:
    res+=str(i)
    
res+=str(even)

final = int(res)

print(final)
    



