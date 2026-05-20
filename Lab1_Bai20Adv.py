tien = [500, 200, 100, 50, 20, 10, 5, 2, 1]


def doi_tien(so_tien):
    tong_to = 0
    tong_loai = 0

    print(f"\nSo tien duoc thoi lai: {so_tien}")
    print("Chi tiet cac loai tien:")

    for i in tien:
        so_to = so_tien // i
        so_tien = so_tien % i

        if so_to > 0:
            print(f"Loai {i} gom {so_to} to")

            tong_to += so_to
            tong_loai += 1

    print(f"TONG CONG CO {tong_to} TO")
    print(f"Tong so loai = {tong_loai}")




a = int(input("Nhap so tien can thanh toan: "))
b = int(input("Nhap so tien khach dua: "))

#thiếu
if a > b:
    print(f"Khach con thieu {a - b} dong")

# đủ
elif a == b:
    print("Cam on khach hang. Hen gap lai!")

# dư
else:
    tien_thoi = b - a

    doi_tien(tien_thoi)

    input("\nNhan Enter de ket thuc...")
    print("Cam on khach hang. Hen gap lai!")