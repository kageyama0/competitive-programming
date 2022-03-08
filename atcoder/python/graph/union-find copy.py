# Union Find
n, m = map(int, input().split())


class UnionFindByRank():
    def __init__(self, n):
        self.par = list(range(n+1))
        self.rank = [0] + [1] + [0]*(n-1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


uf = UnionFindByRank(n)

for _ in range(m):
    x, y = map(int, input().split())
    uf.union(x, y)
    print(uf.par, uf.rank)

print(uf.par)
