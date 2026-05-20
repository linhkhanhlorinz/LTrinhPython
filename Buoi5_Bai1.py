def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

lst = []
while True:
    n = int(input("Nhập một số nguyên dương: "))
    lst.append(n)
    print("Bạn có muốn tiếp tục nhập số không? (y/n): ", end="")
    choice = input()
    if choice != "y" and choice != "Y":
        break
    

print("Các số đã nhập là:", lst)

#a
print("Các số nguyên nguyên tố là:")
for x in lst:
    if prime(x):
        print(x, end=" ")
print()

#b
#trung bình cộng của số âm
am = [x for x in lst if x < 0]
if len(am) > 0:
    avg_negative = sum(am) / len(am)
    print("Trung bình cộng của các số âm là: %.2f" %avg_negative)
else:
    print("Không có số âm nào trong danh sách.")
#trúng bình cộng của số dương
duong = [x for x in lst if x > 0]
if len(duong) > 0:
    avg_positive = sum(duong) / len(duong)
    print("Trung bình cộng của các số dương là: %.2f" %avg_positive)
else:
    print("Không có số dương nào trong danh sách.")

#c 
# số lớn nhất
    max_num = max(lst)
    print("Số lớn nhất là:", max_num)   
# số nhỏ nhất
    min_num = min(lst)  
    print("Số nhỏ nhất là:", min_num)
#d kiểm tra list sắp xếp tăng dần
sosanh = lambda a, b: True if a < b else False
is_sorted = True
for i in range(len(lst)-1):
    if not sosanh(lst[i], lst[i+1]):
        is_sorted = False
        break

if is_sorted:
    print("Danh sách đã được sắp xếp tăng dần.")
else:
    print("Danh sách chưa được sắp xếp tăng dần.")