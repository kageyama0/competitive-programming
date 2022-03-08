import numpy as np

def main():
    n = int(input())
    a = list(map(int, input().split()))
    A = np.array(a)
    B = np.where(A < 0, A * -1, A)
    cnt = np.count_nonzero(A < 0)
    #print(B)
    s = B.sum()
    if cnt % 2 == 0:
        print(s)
    else:
        m = np.amin(A)
        print(s - m)
        

if __name__ == "__main__":
    main()
