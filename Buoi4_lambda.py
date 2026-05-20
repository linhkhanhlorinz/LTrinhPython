import math

#bai a
print("Nhap 1 so nguyen:")
n = int(input())
print(f"Tri tuyet doi cua {n} la: {(lambda x: abs(x))(n)}")

#bai b
print("Nhap 1 so nguyen:")
n = int(input())
print(f"Gtri {n} + 15 la: {(lambda x: x +15)(n)}")

#bai c
print("Nhap so nguyen x:")
x = int(input())
print("Nhap so nguyen y:")
y = int(input())
print(f"Gtri {x} * {y} = {(lambda a,b: a * b)(x,y)}")

#bai d
print("Nhap 1 so nguyen:")
n = int(input())
kq = lambda n: n%13==0 or n%19==0
print(f"Gtri {n} chia het cho 15 hoac 19: {kq(n)}")

#bai e
print("Nhap 1 so thuc-ban kinh hinh tron:")
r = float(input())
print(f"Dt hinh tron ban kinh {r} la: {(lambda x: math.pi*x*x)(r)}")

#bai f
print("Nhap 1 so thuc-chieu dai hcn:")
d = float(input())
print("Nhap 1 so thuc-chieu rong hcn:")
r = float(input())
print(f"Cv hcn rong: {r}, dai:{d}= {(lambda a,b: (a+b)*2)(d,r)}")

#bai g
print("Nhap 1 so nguyen de ktra co phai so chinh phuong ko:")
n = int(input())
kq = lambda n: n>=0 and int((n**0.5))**2==n
print(f"Gtri {n} la so chinh phuong: {kq(n)}")

#bai h
print("Nhap 1 so nguyen de ktra co phai SNT:")
n = int(input())
kq = lambda n: n>=1 and all((n%i!=0) for i in range (2,math.isqrt(n)+1))
print(f"Gtri {n} la so chinh phuong: {kq(n)}")

#bai i
print("Nhap 3 canh cua tam giac:")
a,b,c  = map(int, input().split())
kq = lambda a, b, c: (
    "Khong hop le" if not (a+b>c and a+c>b and b+c>a)
    else "Deu" if a==b==c
    else "Can" if a==b or b==c or a==c
    else "Vuong" if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a
    else "Thuong"
)
print(f"Tam giac la: tam giac {kq(a,b,c)}")
