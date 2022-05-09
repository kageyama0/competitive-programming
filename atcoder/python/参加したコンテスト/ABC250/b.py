N, A, B = map(int, input().split())
graph = [[None] * B * N for _ in range(A * N)]

for i in range(A * N):
    for j in range(B * N):
        if (i // A) % 2 == 0:
            if (j // B) % 2 == 0:
                graph[i][j] = "."
            else:
                graph[i][j] = "#"

        else:
            if (j // B) % 2 == 0:
                graph[i][j] = "#"
            else:
                graph[i][j] = "."

for i in range(A * N):
    print("".join(graph[i]))
