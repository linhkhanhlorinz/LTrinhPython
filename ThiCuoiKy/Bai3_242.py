checkBoiSo = lambda n: n % 13 == 0 or n % 19 == 0

n = int(input("Nhap so nguyen n de ktra phai boi cua 13 hoac 19 ko: "))

if checkBoiSo(n):
   print(n, "la boi so cua 13 hoac 19")
else:
   print(n, "khong phai la boi so cua 13 hoac 19")


checkTriangle = lambda a, b, c: a + b > c and a + c > b and b + c > a

a = int(input("Nhap canh a: "))
b = int(input("Nhap canh b: "))
c = int(input("Nhap canh c: "))

if checkTriangle(a, b, c):
   if a == b == c:
      print("Day la tam giac deu")
   elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
      print("Day la tam giac vuong")
   elif a == b or a == c or b == c:
      print("Day la tam giac can")
   else:
      print("Day la tam giac thuong")
else:
   print(f"{a}, {b}, {c} khong phai la 3 canh cua tam giac")