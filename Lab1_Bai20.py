
tien = [500, 200, 100, 50, 20, 10, 5, 2, 1]


x = int(input("Nhap so tien X: "))

tong_to = 0
tong_loai = 0

print(f"\nSo tien {x} duoc doi thanh:")

for i in tien:
    so_to = x // i
    x = x % i

    if so_to > 0:
        print(f"Loai {i} gom {so_to} to")

        tong_to += so_to
        tong_loai += 1

print(f"TONG CONG CO {tong_to} TO")
print(f"Tong so loai = {tong_loai}")