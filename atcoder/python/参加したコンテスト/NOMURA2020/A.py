def main():
    h1, m1, h2, m2, k = map(int, input().split())
    time = (h2 * 60 + m2) - (h1 * 60 + m1)
    ans = ztime - k
    print(ans)

if __name__ == "__main__":
    main()
