def solve(s,n):
    dic = {}
    for i in range(len(s)):
        if(s[i] in dic.keys()):
            dic[s[i]].append(i)
        else:
            dic[s[i]]=[i]
    
    arr = []
    for key,val in dic.items():
        if(len(val)>=n):
            for i in val:
                arr.append(i)
    
    res = ''
    for i in range(len(s)):
        if(i not in arr):
            res+=s[i]
    return res

s = input()
n = int(input())
s = [i for i in s]
ans = solve(s,n)
print(ans)