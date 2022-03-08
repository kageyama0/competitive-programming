def main():
    N = list(map(int, input().split()))
    for i in range(len(N)):
        if N[i] == 0:
            print(i + 1)
            exit()



if __name__ == "__main__":
    main()
