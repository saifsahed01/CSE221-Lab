#Task A
from queue import Queue
def bfs(G, s, n):
    colour = [0] * (n + 1)
    Q = Queue()
    colour[s] = 1
    Q.put(s)
    order = []
    while not Q.empty():
        u = Q.get()
        order.append(u)
        for v in G[u]:
            if colour[v] == 0:
                colour[v] = 1
                Q.put(v)
    return order
N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
result = bfs(G, 1, N)
print(*result)


#Task B
N, M = map(int, input().split())
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))
adj = [[] for _ in range(N + 1)]
for i in range(M):
    u = u_list[i]
    v = v_list[i]
    adj[u].append(v)
    adj[v].append(u)
visited = [False]*(N+1)
order = []
stack = [1]       
while stack:
    u = stack.pop()
    if not visited[u]:
        visited[u] = True
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                stack.append(v)
print(*order)


#Task C
import queue
N, M, S, D = map(int, input().split())
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))
adj = [[] for _ in range(N + 1)]
for i in range(M):
    u = u_list[i]
    v = v_list[i]
    adj[u].append(v)
    adj[v].append(u)
for i in range(1, N + 1):
    adj[i].sort()
dist = [-1]*(N+1)
parent = [-1]*(N+1)
q = queue.Queue()
dist[S] = 0
parent[S] = S
q.put(S)
while not q.empty():
    node = q.get()
    if node == D:
        break
    for nxt in adj[node]:
        if dist[nxt] == -1:
            dist[nxt] = dist[node] + 1
            parent[nxt] = node
            q.put(nxt)
if dist[D] == -1:
    print(-1)
else:
    path = []
    cur = D
    while True:
        path.append(cur)
        if cur == S:
            break
        cur = parent[cur]
    path.reverse()
    print(dist[D])
    print(*path)


#Task D
import queue
def bfs(start, target, adj, n):
    dist = [-1]*(n+1)
    parent = [-1]*(n+1)
    q = queue.Queue()
    dist[start] = 0
    parent[start] = start
    q.put(start)
    while not q.empty():
        u = q.get()
        if u == target:
            break
        for nxt in adj[u]:
            if dist[nxt] == -1:
                dist[nxt] = dist[u] + 1
                parent[nxt] = u
                q.put(nxt)
    if dist[target] == -1:
        return None, None
    path = []
    cur = target
    while True:
        path.append(cur)
        if cur == start:
            break
        cur = parent[cur]
    path.reverse()
    return dist[target], path
N, M, S, D, K = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
d1, p1 = bfs(S, K, adj, N)
if p1 is None:
    print(-1)
    exit()
d2, p2 = bfs(K, D, adj, N)
if p2 is None:
    print(-1)
    exit()
total_len = d1 + d2
path = p1 + p2[1:]
print(total_len)
print(*path)


#Task E
import sys
input = sys.stdin.readline
N, R = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
subtree = [0]*(N+1)
parent = [-1]*(N+1)
stack = [(R, False)]
parent[R] = 0
while stack:
    node, visited_children = stack.pop()
    if not visited_children:
        stack.append((node, True))
        for nxt in adj[node]:
            if nxt == parent[node]:
                continue
            parent[nxt] = node
            stack.append((nxt, False))
    else:
        total = 1
        for nxt in adj[node]:
            if nxt == parent[node]:
                continue
            total += subtree[nxt]
        subtree[node] = total
Q = int(input())
for _ in range(Q):
    X = int(input())
    print(subtree[X])






