import math

# ==================================================
# a. SỐ THÂN THIỆN
# gcd(n, reverse(n)) == 1
# ==================================================

is_friendly = lambda n: math.gcd(n, int(str(n)[::-1])) == 1


# ==================================================
# b. SỐ CHÍNH PHƯƠNG
# ==================================================

is_square = lambda n: int(math.sqrt(n)) ** 2 == n


# ==================================================
# c1. SỐ ĐỒNG NHẤT (dùng all)
# ==================================================

is_uniform_all = lambda n: all(ch == str(n)[0] for ch in str(n))


# ==================================================
# c2. SỐ ĐỒNG NHẤT (dùng any)
# ==================================================

is_uniform_any = lambda n: not any(
    ch != str(n)[0] for ch in str(n)
)


# ==================================================
# d. SỐ HOÀN THIỆN
# ==================================================

is_perfect = lambda n: (
    n > 1 and
    sum(i for i in range(1, n) if n % i == 0) == n
)


# ==================================================
# IN KẾT QUẢ
# ==================================================

LIMIT = 1_000_000

# --------------------------------------------------
# a. SỐ THÂN THIỆN
# --------------------------------------------------

print("a. SỐ THÂN THIỆN:\n")

for i in range(1, LIMIT + 1):

    if is_friendly(i):
        print(i, end=" ")

print("\n\n")


# --------------------------------------------------
# b. SỐ CHÍNH PHƯƠNG
# --------------------------------------------------

print("b. SỐ CHÍNH PHƯƠNG:\n")

for i in range(1, LIMIT + 1):

    if is_square(i):
        print(i, end=" ")

print("\n\n")


# --------------------------------------------------
# c1. SỐ ĐỒNG NHẤT (ALL)
# --------------------------------------------------

print("c1. SỐ ĐỒNG NHẤT (ALL):\n")

for i in range(1, LIMIT + 1):

    if is_uniform_all(i):
        print(i, end=" ")

print("\n\n")


# --------------------------------------------------
# c2. SỐ ĐỒNG NHẤT (ANY)
# --------------------------------------------------

print("c2. SỐ ĐỒNG NHẤT (ANY):\n")

for i in range(1, LIMIT + 1):

    if is_uniform_any(i):
        print(i, end=" ")

print("\n\n")


# --------------------------------------------------
# d. SỐ HOÀN THIỆN
# --------------------------------------------------

print("d. SỐ HOÀN THIỆN:\n")

for i in range(1, LIMIT + 1):

    if is_perfect(i):
        print(i, end=" ")

# ==================================================
# e. SỐ PHONG PHÚ
# Tổng các ước (không kể chính nó) > n
# ==================================================

is_abundant = lambda n: (
    sum(i for i in range(1, n) if n % i == 0) > n
)


# ==================================================
# f. SỐ TĂNG DẦN
# Các chữ số tăng dần từ trái sang phải
# ==================================================

is_increasing = lambda n: all(
    str(n)[i] <= str(n)[i + 1]
    for i in range(len(str(n)) - 1)
)


# ==================================================
# g. SỐ ARMSTRONG
# ==================================================

is_armstrong = lambda n: (
    sum(
        int(ch) ** len(str(n))
        for ch in str(n)
    ) == n
)


# ==================================================
# h1. SỐ NGUYÊN TỐ
# Cách 1: đếm số ước
# ==================================================

is_prime_1 = lambda n: (
    n > 1 and
    sum(1 for i in range(1, n + 1) if n % i == 0) == 2
)


# ==================================================
# h2. SỐ NGUYÊN TỐ
# Cách 2: tổng ước = n + 1
# ==================================================

is_prime_2 = lambda n: (
    n > 1 and
    sum(i for i in range(1, n + 1) if n % i == 0) == n + 1
)


# ==================================================
# h3. SỐ NGUYÊN TỐ
# Cách 3: kiểm tra chia hết
# ==================================================

is_prime_3 = lambda n: (
    n > 1 and
    not any(
        n % i == 0
        for i in range(2, int(math.sqrt(n)) + 1)
    )
)


# ==================================================
# h4. SỐ NGUYÊN TỐ
# dùng filter + lambda
# ==================================================

def is_prime_4(n):

    if n <= 1:
        return False

    divisors = list(
        filter(
            lambda x: n % x == 0,
            range(2, int(math.sqrt(n)) + 1)
        )
    )

    return len(divisors) == 0


# ==================================================
# i. PALINDROME
# ==================================================

is_palindrome = lambda n: (
    str(n) == str(n)[::-1]
)


# ==================================================
# j. SỐ NGUYÊN TỐ PALINDROME
# ==================================================

is_prime_palindrome = lambda n: (
    is_palindrome(n) and is_prime_3(n)
)


# ==================================================
# k1. SỐ LỘC PHÁT
# dùng all
# ==================================================

is_lucky_all = lambda n: all(
    ch in ['6', '8']
    for ch in str(n)
)


# ==================================================
# k2. SỐ LỘC PHÁT
# đếm số lượng 6 và 8
# ==================================================

is_lucky_count = lambda n: (
    str(n).count('6') + str(n).count('8')
    == len(str(n))
)


# ==================================================
# l. SỐ LỘC PHÁT PALINDROME
# ==================================================

is_lucky_palindrome = lambda n: (
    is_lucky_all(n) and is_palindrome(n)
)


# ==================================================
# e. SỐ PHONG PHÚ
# ==================================================

print("e. SỐ PHONG PHÚ:\n")

for i in range(1, LIMIT + 1):

    if is_abundant(i):
        print(i, end=" ")

print("\n\n")


# ==================================================
# f. SỐ TĂNG DẦN
# ==================================================

print("f. SỐ TĂNG DẦN:\n")

for i in range(1, LIMIT + 1):

    if is_increasing(i):
        print(i, end=" ")

print("\n\n")


# ==================================================
# g. SỐ ARMSTRONG
# ==================================================

print("g. SỐ ARMSTRONG:\n")

for i in range(1, LIMIT + 1):

    if is_armstrong(i):
        print(i, end=" ")

print("\n\n")


# ==================================================
# h. SỐ NGUYÊN TỐ
# ==================================================

print("h. SỐ NGUYÊN TỐ:\n")

for i in range(1, LIMIT + 1):

    if is_prime_3(i):
        print(i, end=" ")

print("\n\n")


# ==================================================
# i. PALINDROME
# ==================================================

print("i. PALINDROME:\n")

for i in range(1, LIMIT + 1):

    if is_palindrome(i):
        print(i, end=" ")

print("\n\n")


# ==================================================
# j. NGUYÊN TỐ PALINDROME
# ==================================================

print("j. NGUYÊN TỐ PALINDROME:\n")

for i in range(1, LIMIT + 1):

    if is_prime_palindrome(i):
        print(i, end=" ")

print("\n\n")


# ==================================================
# k. SỐ LỘC PHÁT
# ==================================================

print("k. SỐ LỘC PHÁT:\n")

for i in range(1, LIMIT + 1):

    if is_lucky_all(i):
        print(i, end=" ")

print("\n\n")


# ==================================================
# l. SỐ LỘC PHÁT PALINDROME
# ==================================================

print("l. SỐ LỘC PHÁT PALINDROME:\n")

for i in range(1, LIMIT + 1):

    if is_lucky_palindrome(i):
        print(i, end=" ")