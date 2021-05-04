s = 'foffrocdroaf'
ana = 'for'
k=len(ana)

dic = {}
uni=0
for i in ana:
    if(i in dic.keys()):
        dic[i]+=1
    else:
        uni+=1
        dic[i]=1
c=100000007
i=0
j=0
while(j<len(s)):
    if( s[j] in dic.keys()):
        dic[s[j]]-=1
        if(dic[s[j]]==0):
            uni-=1 
    if(uni!=0):
        j+=1
    else:
        while(uni==0):
            c = min(c,j-i+1)
            print(s[i:j+1])
            if(s[i] in dic.keys()):
                dic[s[i]]+=1
                if(dic[s[i]]==1):
                    uni+=1
            i+=1
        j+=1
    
print(c)