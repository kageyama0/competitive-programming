import heapq

def main():
    n = int(input())
    #AB = [list(map(int, input().split())) for _ in range(n - 1)]
    #print(AB)

    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(graph)

    visited = [0] * (n + 1)
    q = [1]
    heapq.heapify(q)
    ans = []
    while q:
        now = heapq.heappop(q)
        visited[now] = 1
        ans.append(now)
        #print(q)
        for next in graph[now]:
            print("next:", next)
            print("visited:", visited)
            if visited[next]:
                continue
            heapq.heappush(q,next)
    print(" ".join(map(str,ans)))


if __name__ == "__main__":
    main()
