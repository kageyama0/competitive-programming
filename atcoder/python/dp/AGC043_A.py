def main():
    h, w = map(int, input().split())
    field = [list(input()) for _ in range(h)]
    dp = [[float('inf')] * w for _ in [0] * h]
    dp[0][0] = (field[0][0] == "#")
    # print(dp)
    for i in range(h):
        for j in range(w):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] +
                               (field[i - 1][j] == "." and field[i][j] == "#"))
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] +
                               (field[i][j - 1] == "." and field[i][j] == "#"))
    print(dp[-1][-1])


if __name__ == "__main__":
    main()
