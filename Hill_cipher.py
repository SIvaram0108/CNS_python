def encrypt(text,key_matrix):
    encrypted_text=""
    for i in range(0,len(text),3):
        if i+3<len(text):
            str=text[i:i+3]
        else:
            str=text[i:]+('x'*(3-len(text[i:]))) #to add extra 'x' at end if len of str is less than 3
        matrix=[]
        for j in str:
            matrix.append(ord(j)%65)
        result=[]
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
key_matrix = [];
x = 0
for i in range(3):
    t = []
    for j in range(3):
        t.append(ord(key[x]) % 65)
        x+=1
    key_matrix.append(t)
print("The key is:",key)
encrypted_text=encrypt(text,key_matrix)
print("The text is: " + text)
print("The encrypted text is:",encrypted_text)