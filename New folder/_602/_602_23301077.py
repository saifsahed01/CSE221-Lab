## 10 23301077 CSE-9B-8L-PC4 23301077
import heapq
import sys

def solve():
    try:
        n_str, m_str = sys.stdin.readline().split()
        n, m = int(n_str), int(m_str)
        if not n or not m:
            # Handle cases where n or m might be 0 at the end of input
            return False
    except (IOError, ValueError):
        return False

    u = list(map(int, sys.stdin.readline().split()))
    v = list(map(int, sys.stdin.readline().split()))
    w = list(map(int, sys.stdin.readline().split()))

    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        adj[u[i]].append((v[i], w[i]))

    INF = float('inf')
    dist = [[INF, INF] for _ in range(n + 1)]
    pq = []

    for neighbor, weight in adj[1]:
        parity = weight % 2
        if dist[neighbor][parity] > weight:
            dist[neighbor][parity] = weight
            heapq.heappush(pq, (weight, neighbor, parity))

    while pq:
        d, curr_node, parity = heapq.heappop(pq)

        if d > dist[curr_node][parity]:
            continue

        for neighbor, weight in adj[curr_node]:
            new_parity = weight % 2
            if new_parity == parity:
                new_dist = d + weight
                if new_dist < dist[neighbor][new_parity]:
                    dist[neighbor][new_parity] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor, new_parity))

    result = min(dist[n][0], dist[n][1])

    if result == INF:
        print(-1)
    else:
        print(result)
    
    return True

def main():
    try:
        t_str = sys.stdin.readline()
        if not t_str: return
        t = int(t_str)
        for _ in range(t):
            solve()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()