def main():
    n = int(input())
    ans = []
    m = n if n & 1 else n + 1
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if i + j == m:
                continue
            ans.append([i, j])
    print(ans)



if __name__ == "__main__":
    main()
