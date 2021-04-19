def check(sub):
    if(len(sub)==1):
        return True
    i = 0
    j = len(sub)-1
    while(i<j):
        if(sub[i]!=sub[j]):
            return False
        j-=1
        i+=1
    return True

s = input()
n = len(s)
pali = []
all_sub = []
for i in range(n):
    for j in range(i,n):
        sub = s[i:j+1]
        if( check(sub) ):
            pali.append(sub)

pali.sort()

print(pali[0])  # 0 for min  ,  -1 for max 
