s = input().split(',')

dic = []

for word in s:
    temp = word.split(':')
    val = [i for i in temp[0]]
    key = [int(i) for i in temp[1]]
    su = sum(list(map(lambda x:x**2,key)))
    if(su&1):
        er = val.pop(0)
        val.append(er)
    else:
        er = val.pop()
        val.insert(0,er)
        er = val.pop()
        val.insert(0,er)
    dic.append(''.join(val))
    
print(dic)

#abcd:1234,bcdgfhf:127836,sdjks:1245