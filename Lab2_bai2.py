import math

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

so_luong = 0
for i in range(a, b + 1):
    so_dao_nguoc = int(str(i)[::-1])
    if math.gcd(i, so_dao_nguoc) == 1:
        print(i, end=", " if i < b else "")
        so_luong += 1

print(f"\nSố lượng số thân thiện đã in ra: {so_luong}")