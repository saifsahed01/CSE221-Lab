#Task A
import heapq
def shortest_path(N, M, S, D, u, v, w):
    graph = {i: [] for i in range(1, N + 1)}
    for i in range(M):
        graph[u[i]].append((v[i], w[i]))  
      
    dist = {i: float('inf') for i in range(1, N + 1)}  
    dist[S] = 0
    parent = {i: None for i in range(1, N + 1)}  
    pq = [(0, S)]
    while pq:
        current_dist, u_node = heapq.heappop(pq)
        if current_dist > dist[u_node]:
            continue
        for v_node, weight in graph[u_node]:
            new_dist = current_dist + weight
            if new_dist < dist[v_node]:
                dist[v_node] = new_dist
                parent[v_node] = u_node
                heapq.heappush(pq, (new_dist, v_node))
    if dist[D] == float('inf'):
        return -1, []
    path = []
    current = D
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return dist[D], path
  
N, M, S, D = map(int, input().split())  
u = list(map(int, input().split()))  
v = list(map(int, input().split()))  
w = list(map(int, input().split()))  
distance, path = shortest_path(N, M, S, D, u, v, w)
if distance == -1:
    print(distance)
else:
    print(distance)
    print(" ".join(map(str, path)))



#Task B
import heapq
def dijkstra(N, graph, start):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    pq = [(0, start)] 
    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            new_dist = current_dist + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    return dist
  
def where_to_meet(N, M, S, T, edges):
    graph = {i: [] for i in range(1, N + 1)}
    for u, v, w in edges:
        graph[u].append((v, w))
    dist_from_alice = dijkstra(N, graph, S)
    dist_from_bob = dijkstra(N, graph, T)
    min_time = float('inf')
    meeting_node = -1
    for i in range(1, N + 1):
        if dist_from_alice[i] < float('inf') and dist_from_bob[i] < float('inf'):
            max_time = max(dist_from_alice[i], dist_from_bob[i])
            if max_time < min_time:
                min_time = max_time
                meeting_node = i
    if meeting_node == -1:
        return -1, []
    else:
        return min_time, meeting_node

N, M, S, T = map(int, input().split())  
edges = [tuple(map(int, input().split())) for _ in range(M)]  
time, node = where_to_meet(N, M, S, T, edges)
if time != -1:
    print(time, node)
else:
    print(time)



#Task C
import heapq
def minimize_danger(N, M, roads):
    graph = {i: [] for i in range(1, N + 1)}
    for u, v, w in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))
    danger = [float('inf')] * (N + 1)
    danger[1] = 0
    pq = [(0, 1)]
    while pq:
        current_danger, u = heapq.heappop(pq)
        if current_danger > danger[u]:
            continue
        for v, weight in graph[u]:
            new_danger = max(current_danger, weight)
            
            if new_danger < danger[v]:
                danger[v] = new_danger
                heapq.heappush(pq, (new_danger, v))
    result = []
    for i in range(1, N + 1):
        if danger[i] == float('inf'):
            result.append(-1)
        else:
            result.append(danger[i])
    return result

N, M = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(M)]
result = minimize_danger(N, M, roads)
print(" ".join(map(str, result)))



#Task D
import heapq
def beautiful_path(N, M, S, D, node_weights, edges):
    graph = {i: [] for i in range(1, N + 1)}
    for u, v in edges:
        graph[u].append(v) 
    cost = [float('inf')] * (N + 1)
    cost[S] = node_weights[S - 1]
    pq = [(node_weights[S - 1], S)]  
    while pq:
        current_cost, u = heapq.heappop(pq)
        if current_cost > cost[u]:
            continue
        for v in graph[u]:
            new_cost = current_cost + node_weights[v - 1]
            if new_cost < cost[v]:
                cost[v] = new_cost
                heapq.heappush(pq, (new_cost, v))
    return cost[D] if cost[D] != float('inf') else -1

N, M, S, D = map(int, input().split())
node_weights = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(M)]
result = beautiful_path(N, M, S, D, node_weights, edges)
print(result)



#Task E




#Task F




#Task G
