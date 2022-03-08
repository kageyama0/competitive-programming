n, m = map(int, input().split())
ans = [[0] * m for _ in range(n)]
#print(n, m, ans)
grid = [list(map(int, list(input()))) for _ in range(n)]
#print(grid)

for i in range(n - 2):
  for j in range(1, m - 1):
    if grid[i][j] != 0:
      num = grid[i][j]
      ans[i + 1][j] += num
      grid[i + 2][j] -= num
      grid[i + 1][j + 1] -= num
      grid[i + 1][j - 1] -= num

print(ans)
