p,q=map(int,input("enter two relatively prime numbers ").split()) 
n=p*q 
phi=(p-1)*(q-1)
m=int(input("enter msg : "))
e=int(input("enter e which is prime and less than phi "))
enctext=(m**e)%n 
d=1 
s=s=(d*e)%phi 
while s!=1:
    s=(d*e)%phi  
    d+=1  
d-=1 
dectext=(enctext**d)%n  
print("encrypted text is ",enctext)
print("decrypted text is ",dectext)