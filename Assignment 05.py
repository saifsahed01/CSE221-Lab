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



