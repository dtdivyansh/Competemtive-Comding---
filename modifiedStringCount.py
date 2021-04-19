s = input()

stack = []
res = []

for i in s:
    if(i in stack or not stack):
        stack.append(i)
    else:
        c = len(stack)
        e = int(stack[0])
        res.append( (c,e) )
        stack = []
        stack.append(i)

c = len(stack)
e = int(stack[0])
res.append( (c,e) )

print(res)