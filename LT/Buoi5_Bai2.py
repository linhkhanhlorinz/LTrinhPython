from collections import Counter


def main():
    s1 = input("Nhập chuỗi S1: ")
    s2 = input("Nhập chuỗi S2: ")

    counter1 = Counter(s1)
    counter2 = Counter(s2)

    both_counter = counter1 & counter2
    common_chars = sorted(both_counter.keys())

    only_in_s1 = [ch for ch in dict.fromkeys(s1) if ch not in counter2]
    only_in_s2 = [ch for ch in dict.fromkeys(s2) if ch not in counter1]

    print("\nKết quả:")
    print("a) Các ký tự xuất hiện trong cả S1 và S2:", ", ".join(common_chars) if common_chars else "Không có ký tự chung.")

    print("b) Số ký tự chỉ có trong S1 nhưng không có trong S2:", len(only_in_s1))
    print("   Số ký tự chỉ có trong S2 nhưng không có trong S1:", len(only_in_s2))

    print("c) Ký tự chỉ có trong S1 nhưng không có trong S2:", ", ".join(only_in_s1) if only_in_s1 else "Không có.")
    print("   Ký tự chỉ có trong S2 nhưng không có trong S1:", ", ".join(only_in_s2) if only_in_s2 else "Không có.")


if __name__ == "__main__":
    main()