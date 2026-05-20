from datetime import datetime, timedelta

## cau i
now = datetime.now()

print("Nam:", now.year)
print("Thang:", now.strftime("%B"))
print("Tuan trong nam:", now.isocalendar()[1])
print("Tuan trong thang:", (now.day - 1)//7 + 1)
print("Ngay trong nam:", now.timetuple().tm_yday)
print("Ngay:", now.day)
print("Thu:", now.strftime("%A"))
print("Gio:", now.strftime("%H:%M:%S"))

## cau ii
d1 = int(input("Ngay 1: "))
m1 = int(input("Thang 1: "))
y1 = int(input("Nam 1: "))

d2 = int(input("Ngay 2: "))
m2 = int(input("Thang 2: "))
y2 = int(input("Nam 2: "))

date1 = datetime(y1, m1, d1)
date2 = datetime(y2, m2, d2)

print("So ngay:", abs((date2 - date1).days))

## cau iii
s = input("Nhap (vd: Sep 18 2019 2:43PM): ")
dt = datetime.strptime(s, "%b %d %Y %I:%M%p")
print(dt)

## cau iv
print((now + timedelta(seconds=5)).strftime("%H:%M:%S"))