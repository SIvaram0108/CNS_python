import math 

text=input("Enter any plain text : ").strip() 
text=text.replace(" ","") #replace spaces

length=len(text) 
colsize=4  # any number
rowsize= math.ceil(length/colsize)
l=0 

#make matrix
mat=[] 
for i in range(rowsize):
    temp_row=[] 
    for j in range(colsize):
        if (l<length):
            temp_row.append(text[l])
            l+=1 
        else:
            temp_row.append("")
    mat.append(temp_row)
    
#transpose logic
trans=[["" for i in range(rowsize)] for j in range(colsize)]
for i in range(rowsize):
    for j in range(colsize):
        trans[j][i]=mat[i][j]

print("encrypted text : ", end="")
for i in range(colsize):
    for j in range(rowsize):
        print(trans[i][j],end="")
        
            