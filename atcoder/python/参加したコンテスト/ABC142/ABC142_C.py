def main():
    n = int(input())
    A = list(map(int, input().split()))
    lis = []
    for i, num in enumerate(A):
        lis.append([i + 1, num])
    #print(lis)

    B = sorted(lis, key=lambda x: x[1])
    #print(B)

    for x, _ in B:
        print(x, end=" ")

if __name__ == "__main__":
    main()
