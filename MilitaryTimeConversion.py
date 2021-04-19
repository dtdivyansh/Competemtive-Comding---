time = input().split(':')

hour = int(time[0])

dur = time[2][2:]

if(dur=='PM'):
    hour+=12

res = str(hour)+':'+time[1]+':'+time[2][0:2]

print(res)
