def tripletSum(arr,n):
    if(len(arr)==3):
        print(arr[1])
        return
    choose = n-2
    arr.sort(reverse=True)
    pro = []
    for i in range(choose,len(arr),choose+1):
        pro.append(arr[i])
        if(len(pro)==3):
            break
    print(pro)
    print('sum: ',sum(pro))
    
    
arr = [int(i) for i in input().split()]

n = len(arr)//3

tripletSum(arr, n)
    