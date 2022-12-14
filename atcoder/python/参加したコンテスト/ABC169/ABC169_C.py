# 演算子オーバーロード系はDecimalでくるむ
import decimal


def main():
    a, b = input().split()
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
    print(a * b)


if __name__ == "__main__":
    main()
