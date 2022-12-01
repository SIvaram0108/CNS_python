p=int(input('enter value of p '))
g=int(input('enter value of g '))

a=int(input('enter private key value for a '))
b=int(input('enter private key value for b '))
x=(g**a)%p 
y=(g**b)%p 

ka=(y**a)%p 
kb=(x**b)%p
print("secret key for a is "+str(ka))
print("secret key for b is "+str(kb))