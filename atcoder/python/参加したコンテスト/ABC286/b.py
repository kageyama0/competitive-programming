import re
n = int(input())
s = list(input())

# 全ての"na"を"nya"に置き換える
s = "".join(s).replace("na", "nya")
print(s)
