print("Nhap chuoi bat ky:")
s = input()
print("Nhap tu muon dem:")
w = input()

count = 0
start =0
while True:
   pos = s.find(w,start)
   if(pos == -1):
      break
   count+=1
   start = pos + len(w)
   
print(f"Tu {w}  duoc tim thay {count} lan")