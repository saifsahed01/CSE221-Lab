## 10 23301077 CSE-9B-8L-PC4 23301077
import sys

n = int(input())

for _ in range(n):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    
    flag = False
    left, right = 0, N-1

    while left < right:
        sum = arr[left] + arr[right]
        if sum == S:
            print(left+1, right+1)
            flag = True
            break

        elif sum < S:
            left += 1

        else:
            right -= 1

    if flag == False:
        print(-1)
