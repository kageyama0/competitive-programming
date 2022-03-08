def main():
    s = input()
    s = s.replace("BC", "D")
    #print(s)
    cnt_a = 0
    ans = 0
    for st in s:
        if st == "A":
            cnt_a += 1
        elif st == "D":
            ans += cnt_a
        else:
            cnt_a = 0
    print(ans)


if __name__ == "__main__":
    main()
