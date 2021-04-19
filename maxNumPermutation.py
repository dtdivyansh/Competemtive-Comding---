from itertools import permutations

def fun(arr):
    arr = [str(i) for i in arr]
    tp = permutations(arr)
    #list(tp)
    res = []
    for num in tp:
        val = int(''.join(num))
        res.append(val)
    print(res)
    return max(res)
	       
    
    
    
arr = [3, 3, 1]
a=fun(arr)
print(a)