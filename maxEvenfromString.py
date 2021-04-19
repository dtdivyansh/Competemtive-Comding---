s = input()

arr = [int(i) for i in s if i.isnumeric()]

key = set(arr)

key = list(key)
l=len(key)
key.sort()
res = ''

for i in key:
    if(i%2==0):
        res+=str(i)
        key.remove(i)
        break

if(l==len(key)):
    print(-1)
else:
    for k in key:
        res = str(k) + res
    print(int(res))