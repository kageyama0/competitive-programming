def main():
    n, k = map(int, input().split())
    H = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if H[i] >= k:
            cnt += 1
    print(cnt)



if __name__ == "__main__":
    main()
