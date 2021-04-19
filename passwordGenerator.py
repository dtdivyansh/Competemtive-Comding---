s = input().split(',')

res = ''

for word in s:
    word1 = word.split(':')
    name = word1[0]
    key = [int(k) for k in word1[1]]
    key.sort(reverse=True)
    l = len(name)
    for j in key:
        if(j<=l):
            res+=name[j-1]
            break
    else:
        res+='X'
        
print(res)
        