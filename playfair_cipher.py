def encrypt(text, key):
    alph = "abcdefghiklmnopqrstuvwxyz";
    temp_matrix = []
    for i in key:
        temp_matrix.append(i)
    for i in alph:
        if i not in temp_matrix:
            temp_matrix.append(i)
    matrix = []
    for i in range(5, 26, 5):
        matrix.append(temp_matrix[i - 5:i])
    ind = 0
    encrypted_text = ""
    while (ind < len(text)):
        if ind == len(text) - 1 or text[ind] == text[ind + 1]:
            diagraphX = text[ind]
            diagraphY = "x"
            ind += 1
        else:
            diagraphX = text[ind]
            diagraphY = text[ind + 1]
            ind += 2
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == diagraphX:
                    Xrow = i
                    Xcol = j
                elif matrix[i][j] == diagraphY:
                    Yrow = i
                    Ycol = j
        if Xrow == Yrow:
            encrypted_text += matrix[Xrow][(Xcol + 1) % 5] + matrix[Yrow][(Ycol + 1) % 5]
        elif Xcol == Ycol:
            encrypted_text += matrix[(Xrow + 1) % 5][Xcol] + matrix[(Yrow + 1) % 5][Ycol]
        else:
            encrypted_text += matrix[Xrow][Ycol] + matrix[Yrow][Xcol]
    return encrypted_text


key = "monarchy"
text = "instruments"
encrypted_text = encrypt(text, key)
print(encrypted_text)