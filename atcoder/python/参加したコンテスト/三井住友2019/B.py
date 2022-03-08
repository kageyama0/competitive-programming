def main():
    n = int(input())
    p = n * 25 // 27
    a, b = int(p * 1.08), int((p + 1) * 1.08)
    if a == n:
        print(p)
    elif b == n:
        print(p + 1)
    else:
        print(":(")



if __name__ == "__main__":
    main()
