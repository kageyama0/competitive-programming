import time

def make(S, n):
    if n == k:
        return st
    else:
        return st

def main():
    k, s, t = map(int, input().split())
    lebel_k = "ABC"

    for _ in range(k - 1):
        lebel_k = "A" + lebel_k + "B" + lebel_k + "C"
        print("lebel_k:",lebel_k)
    ans = lebel_k[s - 1:t]
    #print(ans)


if __name__ == "__main__":
    start = time.time()
    main()
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
