N, M, K, S, T, X = map(int, input().split())
MOD = 998244353

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


# Xが何回登場したかを記録しつつ、現在地となるキューをストックしておく二次元配列
q = [[] for _ in range(K)]
q[0].append(S)
# print(q)

for _ in range(K):
    next_q = [[] for _ in range(K)]

    for i in range(K):
        for now in q[i]:
            # print("now", now)
            for next in graph[now]:
                if next == X:
                    next_q[i+1].append(next)
                else:
                    next_q[i].append(next)

            # print("next_q:", next_q)

    q = next_q

ans = 0
for i in range(K):
    if i % 2 == 0:
        ans += q[i].count(T)
        ans %= MOD

print(ans)
