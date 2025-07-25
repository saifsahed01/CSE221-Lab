#Task A
n, S = map(int, input().split())
if not (1 <= n <= 10**6) or not (1 <= S <= 10**9):
    exit()

a = list(map(int, input().split()))

if len(a) != n or any(not (1 <= x <= 10**9) for x in a):
    exit()

i, j = 0, n - 1

while i < j:
    total = a[i] + a[j]
    if total == S:
        print(i + 1, j + 1)
        break
    elif total < S:
        i += 1
    else:
        j -= 1
else:
    print(-1)


#Task B
N, M, K = map(int, input().split())

if not (1 <= N <= 2 * 10**5) or not (1 <= M <= 2 * 10**5) or not (-10**9 <= K <= 10**9):
    exit()

A = list(map(int, input().split()))
B = list(map(int, input().split()))

if len(A) != N or any(not (-10**9 <= x <= 10**9) for x in A):
    exit()

if len(B) != M or any(not (-10**9 <= x <= 10**9) for x in B):
    exit()


i, j = 0, M - 1
closest_i, closest_j = 0, 0
min_diff = float('inf')

while i < N and j >= 0:
    current_sum = A[i] + B[j]
    diff = abs(current_sum - K)
    
    if diff < min_diff:
        min_diff = diff
        closest_i, closest_j = i, j
        
    if current_sum < K:
        i += 1
    else:
        j -= 1

print(closest_i + 1, closest_j + 1)



#Task C
n, x = map(int, input().split())

if not (1 <= n <= 5000) or not (1 <= x <= 10**9):
    exit()
    
arr = list(map(int, input().split()))

if len(arr) != n or not all(1 <= i <= 10**9 for i in arr):
    exit()

for i in range(n - 2):
    target = x - arr[i]
    left, right = i + 1, n - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            print(i + 1, left + 1, right + 1)
            exit()
            
        elif current_sum < target:
            left += 1  
        else:
            right -= 1  
print(-1)



#Task D
n = int(input())
if not (1 <= n <= 10**6):
    exit()

alice_list = list(map(int, input().split()))
if len(alice_list) != n or any(not (-10**9 <= val <= 10**9) for val in alice_list):
    exit()

m = int(input())
if not (1 <= m <= 10**6):
    exit()

bob_list = list(map(int, input().split()))
if len(bob_list) != m or any(not (-10**9 <= val <= 10**9) for val in bob_list):
    exit()
    
i, j = 0, 0
result = []

while i < n and j < m:
    if alice_list[i] <= bob_list[j]:
        result.append(alice_list[i])
        i += 1
    else:
        result.append(bob_list[j])
        j += 1
        
while i < n:
    result.append(alice_list[i])
    i += 1
while j < m:
    result.append(bob_list[j])
    j += 1

for i in result:
    print(i, end=' ')

#Task E
N, K = map(int, input().split())

if not (1 <= N <= 10**5) or not (1 <= K <= 10**9):
    exit()

arr = list(map(int, input().split()))

if len(arr) != N or any(not (1 <= val <= 10**6) for val in arr):
    exit()

left = 0
sum_ = 0
max_length = 0
for right in range(N):
    sum_ += arr[right]
    
    while sum_ > K and left <= right:
        sum_ -= arr[left]
        left += 1
        
    if sum_ <= K:
        if right - left + 1 > max_length:
            max_length = right - left + 1

print(max_length)

#Task F
N, K = map(int, input().split())

if not (1 <= N <= 2*(10**5)) or not (1 <= K <= 10**9):
    exit()

arr = list(map(int, input().split()))

if len(arr) != N or any(not (1 <= val <= 10**6) for val in arr):
    exit()

left = 0
dict1 = {}
max_length = 0

for right in range(N):
    if arr[right] in dict1:
        dict1[arr[right]] += 1
    else:
        dict1[arr[right]] = 1
    
    while len(dict1) > K:
        dict1[arr[left]] -= 1
        if dict1[arr[left]] == 0:
            del dict1[arr[left]] 
        left += 1
    
    if right - left + 1 > max_length:
        max_length = right - left + 1

print(max_length)


#Task G
n, q = map(int, input().split())

if not (1 <= n <= 10**5) or not (1 <= q <= 10**5):
    exit()

arr = list(map(int, input().split()))

if len(arr) != n or any(not (1 <= val <= 10**9) for val in arr):
    exit()

def find_left(x):
    low, high = 0, n
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low

def find_right(y):
    low, high = 0, n
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= y:
            low = mid + 1
        else:
            high = mid
    return low

for i in range(q):
    x, y = map(int, input().split())
    if not (1 <= x <= y <= 10**9):
        exit()
    
    left = find_left(x) 
    right = find_right(y) 
    print(right - left)




#Task H
T = int(input())
if not (1 <= T <= 10**5):
    exit()
    
for y in range(T):
    k, x = map(int, input().split())
    if not (1 <= k <= 10**9) or not (1 < x <= 10**9):
        exit()
        
    i, j = 1, 1
    
    while j < k+1:
        if i%x != 0:
            j += 1
        i += 1    
        
    print(i-1)
