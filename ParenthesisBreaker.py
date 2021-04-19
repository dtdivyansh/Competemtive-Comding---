res = input()

op = '([{'
cl = ')]}'

stack = []

fall = 0

for i in range(len(res)):
    if( res[i] in op ):
        stack.append(res[i])
        fall = i+1
    else:
        t = cl.index(res[i])
        stop = op[t]
        if(stack and stack[-1]!=stop):
            fall = i
            break
        elif(stack and stack[-1]==stop):
            fall = i+1
            stack.pop()
        else:
            stack.append(res[i])
            fall = i
            break
        
if(not stack):
    print(0)          
else:
    print(fall+1)