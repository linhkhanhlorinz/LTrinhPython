S = input("Nhập S='")

all_digits = set("0123456789")

s_digits = set(S)

missing_digits = all_digits - s_digits

result = sorted([int(digit) for digit in missing_digits])

print(f"=>Trong số điện thoại {S} không chứa các ký số: {result}")