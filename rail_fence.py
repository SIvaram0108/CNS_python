plain_text = input("Enter plain text: ").strip()
depth = int(input("Enter depth: "))
cipher_text=''
print("Rail Fence:\n")
for i in range(depth):
    for j in range(i,len(plain_text),depth):
        cipher_text+=plain_text[j]
        print(plain_text[j],end='')
    print()
print("\nCipher text:",cipher_text)