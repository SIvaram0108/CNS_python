message="wearediscoveredsaveyourself"
key="deceptive"
alphabet="abcdefghijklmnopqrstuvwxyz"
e=" "
print("message is: ",message)
print("key is: ",key)
for i in range(len(message)):
    l=(alphabet.index(message[i]) + alphabet.index(key[i%len(key)]))%26
    e=e+alphabet[l]
e=e.strip()
print("encrypted message : "+e)
d=" "
for i in range(len(e)):
    l=(alphabet.index(e[i]) - alphabet.index(key[i%len(key)]))%26
    d=d+alphabet[l]
d=d.strip()
print("decrypted message : "+d)