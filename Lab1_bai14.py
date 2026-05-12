
tien = [500, 200, 100, 50, 20, 10, 5, 2, 1]

x = int(input("Nhap so tien X: "))

tong_to = 0

print(f"\nSo tien {x} duoc doi thanh:")

for i in tien:
    so_to = x // i     
    x = x % i           

    tong_to += so_to

    print(f"Loai {i} gom {so_to} to")

print(f"TONG CONG CO {tong_to} TO")