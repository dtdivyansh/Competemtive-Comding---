num = [int(i) for i in input().split()]

num2 = ''

five = num.index(5)
eight = len(num) - num[::-1].index(8) - 1

num1 = sum(num[:five])

if(eight!=len(num)-1):
    num1+=sum( num[eight+1:] )
    
num2 = ''.join( [str(i) for i in num[five:eight+1]] )
num2 = int(num2)
print(num1,num2)
s = num1+num2

print(s)