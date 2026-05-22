def get_strobo(n, length, is_extended):
    if n == 0:
        return [""]
    if n == 1:
        return ["0", "1", "2", "5", "8"] if is_extended else ["0", "1", "8"]
    
    middles = get_strobo(n - 2, length, is_extended)
    result = []
    
    for mid in middles:
        if n != length:
            result.append("0" + mid + "0")
        result.append("1" + mid + "1")
        result.append("6" + mid + "9")
        result.append("8" + mid + "8")
        result.append("9" + mid + "6")
        if is_extended:
            result.append("2" + mid + "2")
            result.append("5" + mid + "5")
            
    return result

n = int(input("Nhập số nguyên n (2 <= n <= 10): "))

if 2 <= n <= 10:
    arr_a = get_strobo(n, n, False)
    arr_a.sort()
    print(f"a.- Tất cả các số strobogrammatic gồm {n} chữ số:")
    print(", ".join(arr_a))
    
    print()
    
    arr_b = get_strobo(n, n, True)
    arr_b.sort()
    print(f"b.- Tất cả các số strobogrammatic mở rộng gồm {n} chữ số:")
    print(", ".join(arr_b))
else:
    print("Giá trị n không hợp lệ!")