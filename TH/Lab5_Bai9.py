# Bài 9: Tính diện tích đáy và thể tích hình khối chữ nhật

dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))

so_le = int(input("Số lượng số lẻ cần hiển thị: "))

dien_tich_day = dai * rong
the_tich = dai * rong * cao

# Cách 1: dùng round()
print("Cách 1: Diện tích đáy hình chữ nhật =", round(dien_tich_day, so_le), "cm\u00b2")

# Cách 2: dùng format f-string
print(f"Cách 2: Diện tích đáy hình chữ nhật = {dien_tich_day:.{so_le}f}cm\u00b2")

# Cách 1: dùng round()
print("Cách 1: Thể tích hình khối=", round(the_tich, so_le), "cm\u00b3")

# Cách 2: dùng format f-string
print(f"Cách 2: Thể tích hình khối= {the_tich:.{so_le}f}cm\u00b3")