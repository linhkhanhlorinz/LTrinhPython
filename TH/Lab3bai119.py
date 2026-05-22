limit = int(input("Nhập giới hạn: "))
is_prime = [True] * max(2, limit)
is_prime[0] = is_prime[1] = False
for i in range(2, int(limit**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, limit, i):
            is_prime[j] = False

std_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
ext_map = {'0': '0', '1': '1', '2': '2', '5': '5', '6': '9', '8': '8', '9': '6'}

def get_strobo(s, m):
    res = ""
    for c in s:
        if c not in m:
            return None
        res = m[c] + res
    return res

a = []
b = []
c = []
d = []
e = []

for i in range(limit):
    s = str(i)
    
    s_std = get_strobo(s, std_map)
    if s_std == s:
        a.append(str(i))
        if is_prime[i]:
            b.append(str(i))
            
    s_ext = get_strobo(s, ext_map)
    if s_ext == s:
        c.append(str(i))
        if is_prime[i]:
            d.append(str(i))
            
    if s_std is not None and s_std != s and not is_prime[i]:
        if int(s_std) < limit and is_prime[int(s_std)]: 
            e.append(str(i))

print("a. Cac so strobogrammatic:")
print(", ".join(a) + "\n")

print("b. Cac so nguyen to strobogrammatic:")
print(", ".join(b) + "\n")

print("c. Cac so strobogrammatic mo rong:")
print(", ".join(c) + "\n")

print("d. Cac so nguyen to strobogrammatic mo rong:")
print(", ".join(d) + "\n")

print("e. Cac so khong phai strobogrammatic, khong phai nguyen to, nhung strobogrammatic cua no la nguyen to:")
print(", ".join(e) + "\n")