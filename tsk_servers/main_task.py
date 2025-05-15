import heapq

def read_input(filename="gamsrv_in.txt"):
    with open(filename, 'r') as f:
        n, m = map(int, f.readline().split())
        users = set(map(int, f.readline().split()))
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v, w = map(int, f.readline().split())
            graph[u].append((v, w))
            graph[v].append((u, w))
    return n, users, graph

def counting(start, n, graph):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist

def find_optimal_server(n, users, graph):
    min_max_delay = float('inf')

    for candit in range(1, n + 1):
        if candit in users:
            continue
        dist = counting(candit, n, graph)
        max_delay = max(dist[c] for c in users)
        min_max_delay = min(min_max_delay, max_delay)

    return min_max_delay

def write_output(rslt, filename="gamsrv_out.txt"):
    with open(filename, 'w') as f:
        f.write(str(rslt) + '\n')

def main():
    n, users, graph = read_input()
    rslt = find_optimal_server(n, users, graph)
    write_output(rslt)

if __name__ == "__main__":
    main()
