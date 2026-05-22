n_str = input("Nhập số nguyên dương n: ")
S = 0
length = len(n_str)

for i in range(length):
    for j in range(i + 1, length + 1):
        subnumber = int(n_str[i:j])
        S += subnumber ** 2

print(f"S = {S}")