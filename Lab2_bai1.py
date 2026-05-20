cipher_text = input("Nhập cipher text: ")
plain_text = ""
i = 0

while i < len(cipher_text):
    if cipher_text[i] == '#':
        count = int(cipher_text[i+1])
        char = cipher_text[i+2]
        plain_text += char * count
        i += 3
    else:
        plain_text += cipher_text[i]
        i += 1

print("plain text là", plain_text)