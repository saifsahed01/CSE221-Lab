#Task A
import queue
N, M = map(int, input().split())  
prerequisites = [tuple(map(int, input().split())) for _ in range(M)]
adj_list = {}  
in_degree = [0] * (N + 1)  
for A, B in prerequisites:
    if A not in adj_list:
        adj_list[A] = []  
    adj_list[A].append(B)
    in_degree[B] += 1
q = queue.Queue()
for i in range(1, N + 1):
    if in_degree[i] == 0:
        q.put(i)
result = []
while not q.empty():
    course = q.get()  
    result.append(course)
    if course in adj_list:  
        for next_course in adj_list[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                q.put(next_course)  #
if len(result) == N:
    print(*result)
else:
    print(-1)
