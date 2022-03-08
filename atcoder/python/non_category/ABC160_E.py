def main():
    x, y, a, b, c = map(int, input().split())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    R = list(map(int, input().split()))
    t = [1]
    t.sort()
    P.sort(reverse=True)
    Q.sort(reverse=True)
    R.sort(reverse=True)

    s = P[:x] + Q[:y]
    s.sort()
    for i in range(x + y):
        if i < c:
            if s[i] < R[i]:
                s[i] = R[i]
            else:
                break
        else:
            break
    print(sum(s))


if __name__ == "__main__":
    main()
