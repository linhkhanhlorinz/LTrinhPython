<<<<<<< HEAD
dai = input("Nhập chiều dài đáy Hình chữ nhật (cm):")
rong = input("Nhập chiều rộng đáy hình chữ nhật (cm):")
cao = input("Nhap chieu cao hinh khoi chu nhat (cm):")
sole = input("Số lượng số lẻ cần hiển thị:")
dinhdang = '{:.'+sole+'f}'

dai = float(dinhdang.format(eval(dai)))
rong = float(dinhdang.format(eval(rong)))
cao = float(dinhdang.format(eval(cao)))

dientich = dai*rong
dientich = float(dinhdang.format(dientich))
thetich = dai*rong*cao
thetich = float(dinhdang.format(thetich))

print("diện tích đáy hình chữ nhật = ",dientich,"cm\u00b2")
=======
dai = input("Nhập chiều dài đáy Hình chữ nhật (cm):")
rong = input("Nhập chiều rộng đáy hình chữ nhật (cm):")
cao = input("Nhap chieu cao hinh khoi chu nhat (cm):")
sole = input("Số lượng số lẻ cần hiển thị:")
dinhdang = '{:.'+sole+'f}'

dai = float(dinhdang.format(eval(dai)))
rong = float(dinhdang.format(eval(rong)))
cao = float(dinhdang.format(eval(cao)))

dientich = dai*rong
dientich = float(dinhdang.format(dientich))
thetich = dai*rong*cao
thetich = float(dinhdang.format(thetich))

print("diện tích đáy hình chữ nhật = ",dientich,"cm\u00b2")
>>>>>>> c5aeaf5fb15fe6fce27719de659cc0664dac052f
print("Thể tích  khối =",thetich,"cm\u00b3")