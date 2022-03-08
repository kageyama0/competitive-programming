def main():
    s = input()
    l = len(s)
    alp = set(s)

    ans = float('inf')
    for char in alphabets:
        sp = max(map(len, s.split(char)))
        ans = min(ans, sp)
    print(ans)


if __name__ == "__main__":
    main()
