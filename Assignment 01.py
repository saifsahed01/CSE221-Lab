#TASK A
T = int(input())
 if T >= 1 and T <= 100:
    for i in range(T):
        N = int(input())
        if N >= -10**5 and N <= 10**5:
            if N%2 != 0:
                print(N ,'is an Odd number.')
            else:
                print(N ,'is an Even number.')



#TASK B
T = int(input())
if T >= 1 and T <= 1000:
    for i in range(T):
        x = input()
        z = x.split(' ')
        if z[2] == '+':
            print(int(z[1]) + int(z[3]))
        elif z[2] == '-':
            print(int(z[1]) - int(z[3]))
        elif z[2] == '/':
            print(int(z[1]) / int(z[3]))
        elif z[2] == '*':
            print(int(z[1]) * int(z[3]))



#Task C
T = int(input())
if T >= 1 and T <= 10**4:
    for i in range(T):
        N = int(input())
        if N >= 1 and T <= 10**6:
            print(int(N*(N+1)/2))



#TASK D
flag = True
T = int(input())
if T >= 1 and T <= 100:
    for i in range(T):
        l = int(input())
        N = input().split(' ')
        if l >= 1 and l <= 10**4:
            if l == 1:
                print('YES')
            else:
                flag = True
                for j in range(0, l-1):
                    if int(N[j]) >= 1 and int(N[j]) <= 10**6 and int(N[j]) > int(N[j+1]):
                            flag = False
                            break
                if flag:
                    print('YES')
                else:
                    print('NO')
          
          

#TASK E
N = int(input())
array = list(map(int, input().split(" ")))
def reverse(arr, mid):
    arr[mid-1], arr[mid+1] = arr[mid+1], arr[mid-1]
def can_sort(arr):
    n = len(arr)
    Flag = True
    while Flag:
        Flag = False
        for i in range(1, n - 1):
            if arr[i - 1] > arr[i + 1]:
                reverse(arr, i)
                Flag = True
    result="YES"
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            result="NO" 
    return result
print(can_sort(array))

          

#TASK F
def value_check(arr):
    flag = True
    for i in range(len(arr)):
        if arr[i] >= 1 and arr[i] <= 10**6:
            flag = True
        else:
            flag = False
    return flag

N = int(input())
a = list(map(int, input().split()))
if N >= 1 and N <=1000:
    flag = value_check(a)
    if flag:
        flag2 = True
        while flag2:
            flag2 = False
            for i in range(N-1):
                if (a[i]%2 == 0 and a[i+1]%2 == 0) or (a[i]%2 == 1 and a[i+1]%2 == 1):
                    if a[i] > a[i+1]:
                        a[i], a[i+1] = a[i+1], a[i]
                        flag2 = True

for i in a:
    print(i, end = ' ')

          

#TASK G
n = int(input())
id = list(map(int, input().split()))
marks = list(map(int, input().split()))
swaps = 0
students = [(id[i], marks[i]) for i in range(n)]
for i in range(n):
    max_id = i
    for j in range(i+1, n):
        if (students[j][1] > students[max_id][1]) or (students[j][1] == students[max_id][1] and students[j][0] < students[max_id][0]):
                max_id = j  
    if max_id != i:
        students[i], students[max_id] = students[max_id], students[i]
        swaps += 1
print(f"Minimum swaps: {swaps}")
for m, n in students:
        print(f"ID: {m} Mark: {n}")


          
#TASK H
n = int(input())
schedules = []
if n >= 1 and n <=100:
    for idx in range(n):
        line = input().strip()
        parts = line.split()
        train_name = parts[0]
        time_str = parts[-1]
        h, m = map(int, time_str.split(':'))
        minutes = h * 60 + m
        schedules.append((train_name, minutes, idx, line))
    for i in range(1, n):
        key = schedules[i]
        j = i - 1
        while j >= 0:
            if (schedules[j][0] > key[0]) or (schedules[j][0] == key[0] and schedules[j][1] < key[1]) or (schedules[j][0] == key[0] and schedules[j][1] == key[1] and schedules[j][2] > key[2]):
                schedules[j + 1] = schedules[j]
                j -= 1
            else:
                break
        schedules[j + 1] = key
    for i in schedules:
        print(i[3])
