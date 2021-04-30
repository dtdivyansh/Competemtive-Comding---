def pangrams(s):
    alpha = {}
    for i in 'abcdefghijklmnopqrstuvwxyz':
        alpha[i]=1
    for i in s:
        alpha[i.lower()] = 0
   
    val = list(alpha.values())
    su =sum(val)
    
    if(su):
        return 'not pangram'
    else:
        return 'pangram'
