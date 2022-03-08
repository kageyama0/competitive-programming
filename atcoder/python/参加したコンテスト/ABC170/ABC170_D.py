from collections import Counter

def main():
    n = int(input())
    A = list(map(int, input().split()))

    # 複数の同じ値がある場合は消去、
    C = Counter(A)
    non_double_num = []
    double_num = []
    for num, cnt in C.items():
        if cnt != 1:
            double_num += [num]
        else:
            non_double_num += [num]

    non_double_num.sort()
    len_n = len(non_double_num)
    memo = [1] * len_n
    mod_num = 0
    # 割り切れる値も消去
    for i in range(len_n - 1):
        for j in range(i + 1, len_n):
            if memo[j] == 0:
                break
            if non_double_num[j] % non_double_num[i] == 0:
                memo[j] = 0
                mod_num += 1

        for d_n in double_num:
            print(d_n)
            if non_double_num[i] % d_n == 0:
                print(d_n)
                memo[j] = 0
                mod_num += 1

    print(len_n - mod_num)


if __name__ == "__main__":
    main()
