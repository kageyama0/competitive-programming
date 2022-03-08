# 演算子オーバーロード系はDecimalでくるむ
from decimal import *

def main():
    a, b = input().split()
    a = Decimal(a)
    b = Decimal(b)
    print(a * b)





if __name__ == "__main__":
    main()
