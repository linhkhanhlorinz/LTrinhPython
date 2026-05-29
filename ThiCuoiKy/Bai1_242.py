l = float(input("Nhap chieu dai day hinh khoi chu nhat (cm): "))
w = float(input("Nhap chieu rong day hinh khoi chu nhat (cm): "))
h = float(input("Nhap chieu cao hinh khoi chu nhat (cm): "))

pnt = int(input("So luong so le can hien thi: "))

Sday = l * w
TTich = l * w * h

print(f"DT day hinh chu nhat = {Sday:.{pnt}f}cm\u00b2")

print(f"THe tich hinh khoi = {TTich:.{pnt}f}cm\u00b3")