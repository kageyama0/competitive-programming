import time


def main():
    a, b, c, d, e, f = 166.5, 168.2, 177.3, 164.9, 172.0, 165.4
    ave = (a + b + c + d + e + f) / 6
    print(ave)
    s2 = ((a - ave) ** 2 + (b - ave) ** 2 + (c - ave) ** 2 + (d - ave) ** 2 + (e - ave) ** 2 + (f - ave) ** 2) // 6
    print(s2)
    s = s2 ** 0.5
    print(s)


if __name__ == "__main__":
    start = time.time()
    main()
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
