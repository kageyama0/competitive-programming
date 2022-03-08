def main():
    n = int(input())
    A = []
    B = []
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    btn_cnt = 0
    for i in range(n - 1, -1, -1):
        a, b = A[i] + btn_cnt, B[i]
        if b == 1 or a % b == 0:
            continue
        else:
            #print("a:", a + btn_cnt, "b:", b)
            need = b - a % b
            btn_cnt += need
            #print("need:", need)

    print(btn_cnt)


if __name__ == "__main__":
    main()
