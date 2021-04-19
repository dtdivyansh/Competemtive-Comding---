import itertools

def Magic(s):
    arr = []
    arr.extend(s[0])
    arr.extend(s[1])
    arr.extend(s[2])
    mi = 10007
    for m in itertools.permutations(range(1,10)):
        if( sum(m[0:3])==15 and sum(m[0::3])==15 and sum(m[3:6])==15 and sum(m[1::3])==15 and m[0]+m[4]+m[8]==15 and m[2]+m[4]+m[6]==15):
            mi = min( mi , sum(abs( arr[i]-m[i] ) for i in range(9) ) )
    return mi

s = [ [5,3,4],[1,5,8],[6,4,2] ]

print( Magic(s) )