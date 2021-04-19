def rec(S):
    if('.' in S):
        stop = S.index('.')
    else:
        return S[::-1]
    return S[stop-1::-1]+'.'+rec(S[stop+1:])

S = input()
print(rec(S))
    