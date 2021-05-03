s = 'forrfro'
ana = 'for'

k = len(ana)  # WINDOW SIZE

uni = 0

c=0

dic = {}
for i in ana:
    if(i not in dic.keys()):
        dic[i]=1
        uni+=1
    else:
        dic[i]+=1
        
i=0
j=0

while(j<len(s)):
   if(s[j] in dic.keys()):
       if(dic[s[j]]!=0):
           dic[s[j]]-=1
           if(dic[s[j]]==0):
               uni-=1
   if(j-i+1!=k):
       j+=1
   elif(j-i+1==k):
       if(uni==0):
           c+=1
       if(s[i] in dic.keys()):
           if(dic[s[i]]==0):
               uni+=1
           dic[s[i]]+=1
       i+=1
       j+=1
print(c)
            
        