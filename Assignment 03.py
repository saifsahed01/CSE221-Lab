#TASK A
def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    for idx in range(left, right + 1):
        arr[idx] = temp[idx]
    return inv_count
def merge_sort(arr, temp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort(arr, temp, left, mid)
        inv_count += merge_sort(arr, temp, mid + 1, right)
        inv_count += merge(arr, temp, left, mid, right)
    return inv_count
def count_inversions_and_sort(arr):
    n = len(arr)
    temp = [0] * n
    inv_count = merge_sort(arr, temp, 0, n - 1)
    return inv_count, arr
N = int(input())
arr = list(map(int, input().split()))
inv_count, sorted_arr = count_inversions_and_sort(arr)
print(inv_count)
print(*sorted_arr)



#TASK B
def count_special_inversions(arr):
    def merge_sort(l, r):
        if r - l <= 1:
            return 0
        mid = (l + r) // 2
        count = merge_sort(l, mid) + merge_sort(mid, r)
        right_squares = sorted([arr[j] ** 2 for j in range(mid, r)])
        for i in range(l, mid):
            lo, hi = 0, len(right_squares)
            while lo < hi:
                m = (lo + hi) // 2
                if arr[i] > right_squares[m]:
                    lo = m + 1
                else:
                    hi = m
            count += lo
        arr[l:r] = sorted(arr[l:r])
        return count
    return merge_sort(0, len(arr))
N = int(input())
arr = list(map(int, input().split()))
print(count_special_inversions(arr))



#TASK C
def mod_pow(a, b, mod):
    if b == 0:
        return 1
    half = mod_pow(a, b // 2, mod)
    result = (half * half) % mod
    if b % 2 == 1:
        result = (result * a) % mod
    return result
a, b = map(int, input().split())
print(mod_pow(a, b, 107))



#TASK D
MOD = 10**9 + 7
def mat_pow(a11, a12, a21, a22, n):
    r11, r12, r21, r22 = 1, 0, 0, 1 
    A11, A12, A21, A22 = a11, a12, a21, a22
    while n > 0:
        if n % 2 == 1:
            t11 = (r11 * A11 + r12 * A21) % MOD
            t12 = (r11 * A12 + r12 * A22) % MOD
            t21 = (r21 * A11 + r22 * A21) % MOD
            t22 = (r21 * A12 + r22 * A22) % MOD
            r11, r12, r21, r22 = t11, t12, t21, t22
        t11 = (A11 * A11 + A12 * A21) % MOD
        t12 = (A11 * A12 + A12 * A22) % MOD
        t21 = (A21 * A11 + A22 * A21) % MOD
        t22 = (A21 * A12 + A22 * A22) % MOD
        A11, A12, A21, A22 = t11, t12, t21, t22
        n //= 2 
    return r11, r12, r21, r22
T = int(input()) 
for _ in range(T):
    a11, a12, a21, a22 = map(int, input().split())
    x = int(input())
    r11, r12, r21, r22 = mat_pow(a11, a12, a21, a22, x)
    print(f"{r11} {r12}")
    print(f"{r21} {r22}")



#TASK E
def fast_series_sum(a, n, m):
    if n == 1:
        return a % m, a % m
    if n % 2 == 0:
        S_half, P_half = fast_series_sum(a, n // 2, m)
        S = (S_half + (P_half * S_half) % m) % m
        P = (P_half * P_half) % m
        return S, P
    else:
        S_prev, P_prev = fast_series_sum(a, n - 1, m)
        S = (S_prev + (P_prev * a) % m) % m
        P = (P_prev * a) % m
        return S, P
 
T = int(input())
for _ in range(T):
    a, n, m = map(int, input().split())
    ans, _ = fast_series_sum(a, n, m)
    print(ans)


#TASK F
def bst_order(arr, l, r, res):
    if l > r:
        return
    mid = (l + r) // 2
    res.append(arr[mid])
    bst_order(arr, l, mid - 1, res)
    bst_order(arr, mid + 1, r, res)
 
n = int(input())
arr = list(map(int, input().split()))
res = []
bst_order(arr, 0, n - 1, res)
for x in res:
    print(x, end = ' ')



#TASK G
n = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))
 
index = {v: i for i, v in enumerate(inorder)}
res = []
 
def solve(il, ir, pl, pr):
    if il > ir or pl > pr:
        return
    root = preorder[pl]
    k = index[root]
    left = k - il
    solve(il, k-1, pl+1, pl+left)
    solve(k+1, ir, pl+left+1, pr)
    res.append(root)
 
solve(0, n-1, 0, n-1)
print(*res)

#Task H
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
 
index = {v: i for i, v in enumerate(inorder)}
res = []
 
def solve(il, ir, pl, pr):
    if il > ir or pl > pr:
        return
    root = postorder[pr]
    res.append(root)
    k = index[root]
    left = k - il
    solve(il, k-1, pl, pl+left-1)
    solve(k+1, ir, pl+left, pr-1)
 
solve(0, n-1, 0, n-1)
print(*res)

