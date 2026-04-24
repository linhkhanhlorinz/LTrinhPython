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
