s = input()
k = int(input())

dic = []

for i in range(k):
    dic.append({s[i]:1})
    
i=0
j=k

while(j<len(s)):
    t = i%k
    if(s[j] in dic[t].keys()):
        dic[t][s[j]]+=1
    else:
        dic[t][s[j]]=1
    i+=1
    j+=1
    
print(dic)
cost=0
for d in dic:
    l = list(d.values())
    if(len(l)==1):
        continue
    l.remove(max(l))
    cost+=sum(l)
    
print(cost)