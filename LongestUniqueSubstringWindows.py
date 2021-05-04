s = 'ababcebecfdbebe'
k = 3

dic = {}

i=0
j=0

mx=0

while(j<len(s)):
    if(s[j] not in dic.keys()):
        dic[s[j]]=1
        mx = max(mx,len(dic))
        j+=1
    else:
        if(s[i] in dic.keys() ):
            dic.pop(s[i])
        i+=1
    
print(mx)