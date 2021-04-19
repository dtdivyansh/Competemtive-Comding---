import re

s = input()

ones = re.findall('[aAbdDeoOpPqQ4690]',s)
twos = re.findall('[8B]',s)

print(ones,twos)

val = len(ones) + len(twos)*2

print(val)
