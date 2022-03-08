def main():
    n = int(input())
    A = [0] + [int(input()) for _ in [0] * n]
    visited = [0] * (n+1)
    now = 1
    visited[now] = 1
    cnt = 0
    while True:
        next = A[now]
        cnt += 1
        if visited[next]:
            print(-1)
            break

        if next == 2:
            print(cnt)
            break

        visited[next] = 1
        now = next


if __name__ == "__main__":
    main()
