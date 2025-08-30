import heapq
import sys

def solve():
    try:
        line1 = sys.stdin.readline().strip()
        if not line1: return False
        n, m, s, d = map(int, line1.split())
    except (IOError, ValueError):
        return False

    weights = [0] + list(map(int, sys.stdin.readline().strip().split()))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().strip().split())
        adj[u].append(v)

    INF = float('inf')
    dist = [INF] * (n + 1)
    
    if s == d:
        print(weights[s])
        return True

    dist[s] = weights[s]
    pq = [(weights[s], s)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v in adj[u]:
            new_dist = current_dist + weights[v]
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    result = dist[d]

    if result == INF:
        print(-1)
    else:
        print(result)

    return True

def main():
    try:
        t_str = sys.stdin.readline().strip()
        if not t_str: return
        t = int(t_str)
        for _ in range(t):
            solve()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()