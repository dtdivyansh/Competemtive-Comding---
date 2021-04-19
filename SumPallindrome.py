def checkPalindrome(s):
    i = 0
    j = len(s)-1
    while(i<j):
        if(s[i]!=s[j]):
            return False
        i+=1
        j-=1
    return True

n = input()

while(True):
    rev = int(n[::-1])
    num = int(n)
    s = num+rev
    if(checkPalindrome(str(s))):
        print('Palindrome: ',s )
        break
    else:
        n = str(s)
    