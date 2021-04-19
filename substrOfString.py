dp = [[0 for i in range(5+1)] for j in range(5+1)]

def sub(s,i,j):
    global dp
    if(len(s)==0 or i<0 or j<0):
        return ''
    else:
        if(not dp[i][j] and s[i:j]!=''):
            print(s[i:j])
            dp[i][j]=1
        sub(s,i,j-1)
        sub(s,i-1,j)
        
    
sub('abcde',5,5)