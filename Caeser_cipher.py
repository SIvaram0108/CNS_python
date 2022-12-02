def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + s - 65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result


text = "hello world"
s = 31
encrypted_text = encrypt(text, s)
print("encrypted text : " + encrypted_text)
decrypted_text = encrypt(encrypted_text, 26 - s)
print("decrypted text : " + decrypted_text)
