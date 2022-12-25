# Union Find
n, m = map(int, input().split())
root = list(range(n + 1))
depth = [0] * (n + 1)


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


uf = UnionFind(n)
# print(uf.parents)
print(uf)

for _ in range(m):
    x, y = map(int, input().split())
    uf.union(x-1, y-1)

# print(uf.members(0))

for i in range(n):
    if i not in uf.members(0):
        print("No")
        exit()

print("Yes")
