n = int(input())
a = []
xy = []
for i in range(n):
    a.append(int(input()))
    xy.append([list(map(int, input().split())) for _ in range(a[-1])])

# bfs,dfs ?->try dfs
def dfs(seen_, i):  # iの人が正直者だと仮定する。i=0,1,2,...,n-1
seen = seen_.copy()
seen[i] = 1  # -1:未定、1:正直者、0:不親切
todo = []
todo.append(i)
while len(todo) > 0:
    b = todo.pop()
    if seen[b] == 1:
        l = xy[b]
        for li in l:
        if seen[li[0]-1] == -1:
            seen[li[0]-1] = li[1]
            if li[1] == 1:
                todo.append(li[0]-1)
            elif seen[li[0]-1] != li[1]:
                seen_[i] = 0
                return seen_
  return seen


ans = 0
for i in range(n):
    seen = [-1]*n
    seen[i] = 1
    seen = dfs(seen, i)
    #print(i,seen)
    while seen.count(-1) > 0:
        j = [k for k, v in enumerate(seen) if v == -1][0]
        seen = dfs(seen, j)
    ans = max(ans, seen.count(1))
print(ans)
