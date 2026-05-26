import math

# ==================================================
# HÀM HỖ TRỢ: TỔNG ƯỚC KHÔNG KỂ CHÍNH NÓ
# Ví dụ: n = 28
# Ước không kể nó: 1, 2, 4, 7, 14
# Tổng = 28
# ==================================================

def sum_proper_divisors(n):
    if n <= 1:
        return 0

    total = 1

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i

            other = n // i
            if other != i:
                total += other

    return total


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
# c1. SỐ ĐỒNG NHẤT - dùng all
# Ví dụ: 111, 2222, 99999
# ==================================================

is_uniform_all = lambda n: all(
    ch == str(n)[0]
    for ch in str(n)
)


# ==================================================
# c2. SỐ ĐỒNG NHẤT - dùng any
# ==================================================

is_uniform_any = lambda n: not any(
    ch != str(n)[0]
    for ch in str(n)
)


# ==================================================
# d. SỐ HOÀN THIỆN
# Tổng các ước không kể chính nó = chính nó
# Ví dụ: 6, 28, 496
# ==================================================

is_perfect = lambda n: n > 1 and sum_proper_divisors(n) == n


# ==================================================
# e. SỐ PHONG PHÚ
# Tổng các ước không kể chính nó > chính nó
# ==================================================

is_abundant = lambda n: sum_proper_divisors(n) > n


# ==================================================
# f. SỐ TĂNG DẦN
# Các chữ số tăng dần hoặc bằng nhau từ trái sang phải
# Ví dụ: 123, 118, 5679
# ==================================================

is_increasing = lambda n: all(
    str(n)[i] <= str(n)[i + 1]
    for i in range(len(str(n)) - 1)
)


# ==================================================
# g. SỐ ARMSTRONG
# Ví dụ: 153 = 1^3 + 5^3 + 3^3
# ==================================================

is_armstrong = lambda n: sum(
    int(ch) ** len(str(n))
    for ch in str(n)
) == n


# ==================================================
# h1. SỐ NGUYÊN TỐ - cách 1: đếm số ước
# ==================================================

is_prime_1 = lambda n: (
    n > 1 and
    sum(1 for i in range(1, n + 1) if n % i == 0) == 2
)


# ==================================================
# h2. SỐ NGUYÊN TỐ - cách 2: tổng ước = n + 1
# ==================================================

is_prime_2 = lambda n: (
    n > 1 and
    sum(i for i in range(1, n + 1) if n % i == 0) == n + 1
)


# ==================================================
# h3. SỐ NGUYÊN TỐ - cách 3: kiểm tra chia hết
# Tối ưu hơn vì chỉ kiểm tra tới căn bậc hai của n
# ==================================================

is_prime_3 = lambda n: (
    n > 1 and
    not any(
        n % i == 0
        for i in range(2, int(math.sqrt(n)) + 1)
    )
)


# ==================================================
# h4. SỐ NGUYÊN TỐ - dùng filter + lambda
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
# Số đọc xuôi và ngược giống nhau
# Ví dụ: 121, 1331
# ==================================================

is_palindrome = lambda n: str(n) == str(n)[::-1]


# ==================================================
# j. SỐ NGUYÊN TỐ PALINDROME
# ==================================================

is_prime_palindrome = lambda n: is_palindrome(n) and is_prime_3(n)


# ==================================================
# k1. SỐ LỘC PHÁT - dùng all
# Chỉ chứa chữ số 6 và 8
# Ví dụ: 6, 8, 66, 68, 86, 88
# ==================================================

is_lucky_all = lambda n: all(
    ch in ['6', '8']
    for ch in str(n)
)


# ==================================================
# k2. SỐ LỘC PHÁT - dùng count
# ==================================================

is_lucky_count = lambda n: (
    str(n).count('6') + str(n).count('8') == len(str(n))
)


# ==================================================
# l. SỐ LỘC PHÁT PALINDROME
# ==================================================

is_lucky_palindrome = lambda n: is_lucky_all(n) and is_palindrome(n)


# ==================================================
# HÀM IN KẾT QUẢ
# ==================================================

def print_numbers(title, condition, limit):
    print(title)
    print("-" * 50)

    count = 0

    for i in range(1, limit + 1):
        if condition(i):
            print(i, end=" ")
            count += 1

    print()
    print("Tổng cộng:", count, "số")
    print("\n")


# ==================================================
# CHƯƠNG TRÌNH CHÍNH
# ==================================================

LIMIT = 1_000_000

print_numbers("a. SỐ THÂN THIỆN", is_friendly, LIMIT)

print_numbers("b. SỐ CHÍNH PHƯƠNG", is_square, LIMIT)

print_numbers("c1. SỐ ĐỒNG NHẤT - dùng all", is_uniform_all, LIMIT)

print_numbers("c2. SỐ ĐỒNG NHẤT - dùng any", is_uniform_any, LIMIT)

print_numbers("d. SỐ HOÀN THIỆN", is_perfect, LIMIT)

print_numbers("e. SỐ PHONG PHÚ", is_abundant, LIMIT)

print_numbers("f. SỐ TĂNG DẦN", is_increasing, LIMIT)

print_numbers("g. SỐ ARMSTRONG", is_armstrong, LIMIT)

print_numbers("h. SỐ NGUYÊN TỐ", is_prime_3, LIMIT)

print_numbers("i. PALINDROME", is_palindrome, LIMIT)

print_numbers("j. SỐ NGUYÊN TỐ PALINDROME", is_prime_palindrome, LIMIT)

print_numbers("k. SỐ LỘC PHÁT", is_lucky_all, LIMIT)

print_numbers("l. SỐ LỘC PHÁT PALINDROME", is_lucky_palindrome, LIMIT)