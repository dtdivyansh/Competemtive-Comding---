def findMat2x2(arr,n,n2):
    if n<2:
        return []
    else:
        final = []
        for i in range(n-1):
            for j in range(n2-1):
                a1 = arr[i][j]
                a2 = arr[i][j+1]
                a3 = arr[i+1][j]
                a4 = arr[i+1][j+1]
                s = []
                val = [a1,a2,a3,a4]
                for num in val:
                    su = 0
                    while(num>0):
                        su = su+(num%10)
                        num = num//10
                    s.append(su)
                
                temp = 1
                for v in range(len(val)):
                    if( val[v]%s[v]!=0 ):
                        temp = 0
                        break
                if(temp):
                    final.append([[a1,a2],[a3,a4]])
                #else:
                 #   continue
        return final
                
arr = [ [43,55,32],[30,24,27],[13,19,40],[11,277,13] ]
n=len(arr)
n2 = len(arr[0])
                   
out = findMat2x2(arr, n,n2) 

print(out)
                