delete = int(input())
arr = [int(i) for i in input()]

val = []

s = set(arr)
s = list(s)

for i in s:
    val.append(arr.count(i))
    
val.sort()

for i in range(len(val)):
    for j in range(0,val[i]):
        if(delete<=0):
            break
        val[i]-=1
        delete-=1
    if(delete<=0):
        break

c = 0

for i in val:
    if(i!=0):
        c+=1
print(c)