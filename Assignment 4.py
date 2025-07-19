#TASK A
N, M = map(int, input().split())
matrix = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    ui, vi, wi = map(int, input().split())
    matrix[ui-1][vi-1] = wi  # -1 for 0-based indexing
for row in matrix:
    print(' '.join(map(str, row)))



#TASK B
N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))
adj = [[] for _ in range(N + 1)]  
for i in range(M):
    adj[u[i]].append((v[i], w[i]))
for i in range(1, N + 1):
    line = f"{i}:"
    if adj[i]:
        line += " ".join(f"({x[0]},{x[1]})" for x in adj[i])
    print(line)


  
#TASK C
N = int(input())
matrix = [[0]*N for _ in range(N)]
for i in range(N):
    data = list(map(int, input().split()))
    k = data[0]
    for j in range(1, k+1):
        matrix[i][data[j]] = 1
for row in matrix:
    print(' '.join(map(str, row)))



#TASK D
N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
degree = [0] * (N + 1)  
for i in range(M):
    degree[u[i]] += 1
    degree[v[i]] += 1
odd = 0
for d in degree[1:]:
    if d % 2 == 1:
        odd += 1
if odd in [0, 2]:
    print("YES")
else:
    print("NO")



#TASK E
n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
incoming = [0] * (n + 1)    
outgoing = [0] * (n + 1)
for i in range(m):
    outgoing[u[i]] += 1
    incoming[v[i]] += 1
result = []
for i in range(1, n + 1):
    result.append(str(incoming[i] - outgoing[i]))
print(' '.join(result))



#TASK F
N = int(input())
x, y = map(int, input().split())
valid = []
for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
        if dx == 0 and dy == 0:
            continue 
        nx, ny = x + dx, y + dy
        if 1 <= nx <= N and 1 <= ny <= N:
            valid.append((nx, ny))
print(len(valid))
for nx, ny in valid:
    print(nx, ny)



#TASK G
N, M, K = map(int, input().split())
board = []
for _ in range(N + 1):
    board.append([0] * (M + 1))
knights = []
for _ in range(K):
    x, y = map(int, input().split())
    board[x][y] = 1
    knights.append((x, y))
moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (1, -2), (1, 2), (2, -1), (2, 1)]
for x, y in knights:
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= N and 1 <= ny <= M and board[nx][ny]:
            print("YES")
            exit()
print("NO")

  

#TASK H
import math
N, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i != j and math.gcd(i, j) == 1:
            graph[i].append(j)
for _ in range(Q):
    X, K = map(int, input().split())
    if len(graph[X]) >= K:
        print(graph[X][K-1])
    else:
        print(-1)
