def find_first_repeated_word(s):
    words = s.split()
    
    seen_words = set()
    
    for word in words:
        if word in seen_words:
            return word
        
        seen_words.add(word)
        
    return None

S = input('Nhập chuỗi S = ')

result = find_first_repeated_word(S)
print(f"Kết quả sẽ in ra: {result}")