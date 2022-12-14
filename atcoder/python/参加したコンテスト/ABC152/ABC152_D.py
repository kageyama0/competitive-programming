from collections import defaultdict


def main():
    n = int(input())
    d = defaultdict(int)
    for i in range(n):
        num = str(i + 1)
        head = num[0]
        tail = num[-1]
        d[(head, tail)] += 1

    l = list(d.items())
    ans = 0
    for (head, tail), cnt in l:
        ans = cnt * d[(tail, head)]
    print(ans)


if __name__ == "__main__":
    main()
