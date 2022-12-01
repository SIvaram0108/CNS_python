def encrypt(text,key):
    encrypted_text=""
    key_matrix = [];matrix=[];result=[]
    x = 0
    for i in range(3):
        t = []
        for j in range(3):
            t.append(ord(key[x]) % 65)
            x+=1
        key_matrix.append(t)
    for j in text:
        matrix.append(ord(j)%65)
    for j in range(3):
        s=0
        for k in range(3):
            s+=key_matrix[j][k]*matrix[k]
        result.append(s)
    for j in result:
        encrypted_text+=chr((j%26)+65)
    return encrypted_text
text="ACT"
key="GYBNQKURP"
print("The key is:",key)
encrypted_text=encrypt(text,key)
print("The text is: " + text)
print("The encrypted text is:",encrypted_text)