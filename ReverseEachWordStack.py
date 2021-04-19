def reverseWords(S):
    res = ''
    stack = []
    for i in S:
        if(i=='.'):
            while(stack):
                res+=stack.pop()
            res+='.'
        else:
            stack.append(i)
            
    while(stack):
        res+=stack.pop()
    return res
                
    
    
S = input()
print(reverseWords(S))
