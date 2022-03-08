def main():
    s = input()
    ans = [1] * len(s)
    for i in range(len(s)-2):
        if s[i] == 'R' and s[i+1] == 'R':
            ans[i+2] += ans[i]
            ans[i] = 0
    for i in range(len(s)-1, 1, -1):
        if s[i] == 'L' and s[i-1] == 'L':
            ans[i-2] += ans[i]
            ans[i] = 0
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
  main()
