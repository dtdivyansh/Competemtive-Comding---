s = 'aaabcebebebe'
k = 3

dic = {}

i=0
j=0

mx=0

while(j<len(s)):
    if(s[j] in dic.keys()):
        dic[s[j]]+=1
    else:
        dic[s[j]]=1
        
    if(len(dic)==k):
        print(s[i:j+1])
        mx = max(mx,j-i+1)
        j+=1
        
    elif(len(dic)<k):
        j+=1
        
    else:
        while(len(dic)>k):
            dic[s[i]]-=1
            if(dic[s[i]]==0):
                dic.pop(s[i])
            i+=1
            
        if(len(dic)<k):
            j+=1
        else:
            print(s[i:j+1])
            mx = max(mx,j-i+1)
            j+=1
            
print(mx)