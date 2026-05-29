def xuLyChuoi():
   chuoi = input("Nhap vao 2 so nguyen a va b, cach nhau boi dau \",\": ")

   a,b = chuoi.strip().split(',')
   a = int(a)
   b = int(b)
   return a,b
   
def inBCC(a,b):
   mi = min(a, b)
   ma = max(a,b)
   print(f"Bang cuu chuong {mi} den {ma}:")
   for i in range(mi,ma+1):
      print(f"Bang cuu chuong {i}:")
      for u in range(1,11):
         print(f"{i} * {u} = {i*u}") 



def isPrime(n):
   if n < 2:
      return False
   if n == 2:
      return True
   
   for i in range(2, int(n**0.5 + 1)):
      if n % i ==0:
         return False
   return True


def primeBHn(n):
   ds = []
   print(f"Cac snt < {n}: ")
   for i in range(2,n):
      if isPrime(i):
         ds.append(i)
   for x in range(len(ds)):
      print(ds[x])


def divisorAndPrime(n):
   lst = []
   for i in range(1, n+1):
      if n % i==0 and isPrime(i):
         lst.append(i)

   print(f"vua la uoc so cua {n} vua la snt: ")

   for x in range (len(lst)):
      print(lst[x])


n = int(input("Nhap so nguyen duong n: "))
primeBHn(n)
divisorAndPrime(n)

a,b = xuLyChuoi() 
inBCC(a,b)