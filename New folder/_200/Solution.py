import sys


def merge(l,r):
    i, j = 0,0
    lst = []
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            lst.append(l[i])
            i+=1
        else:
            lst.append(r[j])
            j+=1
    
    while j < len(r):
        lst.append(r[j])
        j+=1
    
    while i < len(l):
        lst.append(l[i])
        i+=1

    return lst


n = int(input())

for i in range(n):
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    lst1 = merge(A,B)

    if not(1<=max(N,M)<=500000) or not(1<=K<=N+M):
        exit()
    
    if not any(1<=i<=1000000000 for i in A) or not any(1<=j<=1000000000 for j in B):
        exit()

    print(lst1[K-1])


