s = input()
size = len(s)

l = size//2

while(l>0):
    pref = s[:l]
    suff = s[size-l:]
    if(pref==suff):
        print(l)
        break
    else:
        l-=1