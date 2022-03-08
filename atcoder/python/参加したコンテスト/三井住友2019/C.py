def main():
    x = int(input())
    cnt = x // 100
    m, M = cnt * 100, cnt * 105
    if m <= x <= M:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
