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

