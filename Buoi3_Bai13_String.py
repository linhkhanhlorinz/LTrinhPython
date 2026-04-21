##print("Nhap chuoi bat ky:")
##s = input()
s = """     Áo    đỏ em đi giữa phố đông,
Cây xanh như cũng ánh theo hồng.
Em đi lửa   cháy trong      bao mắt  ,
Anh đứng thành    tro em biết không       ?"""

s = s.strip()
s = " ".join(s.split())
s = s.replace(" ,",", ")
s = s.replace(" .",". ")
print(s)
