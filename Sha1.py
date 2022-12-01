import hashlib

print("Sha1 algorithm")
string = input("Enter the input string : ").strip()
text = hashlib.sha1(string.encode('ASCII'))
encrypt = text.hexdigest()
print("Encrypted string is : "+encrypt)