def main():
    n = int(input())
    A = []
    B = []
    for _ in range(n):
        a, b = map(int, input().split())
        A += [a]
        B += [b]
    A.sort()
    B.sort()

    if n % 2 == 0:
        mid_pos = n // 2
        mid_A = A[mid_pos - 1] + A[mid_pos]
        mid_B = B[mid_pos - 1] + B[mid_pos]
        cnt = mid_B - mid_A + 1
    else:
        mid_pos = (n + 1) // 2 - 1
        mid_A = A[mid_pos]
        mid_B = B[mid_pos]
        cnt = mid_B - mid_A + 1
    print(cnt)

if __name__ == "__main__":
    main()
