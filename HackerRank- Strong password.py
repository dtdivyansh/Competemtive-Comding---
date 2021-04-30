def minimumNumber(n, password):
    satisfy = [0,1,1,1,1]
    p=0
    if(n<6):
        p = 6-n
    
    for i in password:
        if(i.isupper()):
            satisfy[3]=0
        elif(i.islower()):
            satisfy[2]=0
        elif(i.isdigit()):
            satisfy[1]=0
        elif(i in "!@#$%^&*()-+"):
            satisfy[4]=0
    return max(sum(satisfy),p)
