def sol(V,s):
    stack=[i for i in s]
    for j in V:
        if(j==stack[0]):
            stack.pop(0)
        if(not stack):
            break
    if(stack):
        return 'NEGATIVE'
    else:
        return 'POSITIVE'

V = 'coronavirus'
n=int(input())

blood = []

for i in range(n):
    blood.append(input())
    
res = []

for i in range(n):
    x = sol(V,blood[i])
    res.append(x)
    
print(res)