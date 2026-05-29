#cach 1 dung all
isSameNumber1 = lambda n: all(x == str(n)[0] for x in str(n))
# c2 dung any
isSameNumber2 = lambda n: any(n == int(str(i) * k) for k in range(1, 6) for i in range(1, 10))

isPerfect = lambda n: n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

print("Cach 1/ so dong nhat tu 1 den 10000:")
for i in range(1, 10001):
   if isSameNumber1(i):
      print(i, end=" ")

print("\nCach 2/ so dong nhat tu 1 den 10000:")
for i in range(1, 10001):
   if isSameNumber2(i):
     print(i, end=" ")

print("\nCac so hoan thien tu 1 den 10000:")
for i in range(1, 10001):
   if isPerfect(i):
     print(i)