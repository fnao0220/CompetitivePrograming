def YN(cond):
    return "Yes" if cond else "No"

row_matrix = []
column_matrix = []
matrix_matrix = []

for i in range(9):
    row_matrix.append(list(map(int, input().split())))

column_matrix = [[row[i] for row in row_matrix] for i in range(len(row_matrix[0]))]

for i in range(0, 9, 3):  # 行のインデックスを3つずつ増やす
    for j in range(0, 9, 3):  # 列のインデックスを3つずつ増やす
        subgrid = []
        for row in range(3):  # 3行を取得
            subgrid.append(row_matrix[i + row][j:j + 3])  # 3列を取得
        matrix_matrix.append(subgrid)
        

cond_1 = True
cond_2 = True
cond_3 = True

cond_array = [1,2,3,4,5,6,7,8,9]
# 条件１
for row in row_matrix:
    cond_1 = True
    cond_array = [1,2,3,4,5,6,7,8,9]
    for cell in row:
        if cell in cond_array:
            cond_array.remove(cell)
        else:
            cond_1 = False
            break
    if not cond_1:
        break

# 条件２
for clm in column_matrix:
    cond_2 = True
    cond_array = [1,2,3,4,5,6,7,8,9]
    for cell in clm:
        if cell in cond_array:
            cond_array.remove(cell)
        else:
            cond_2 = False
            break
    if not cond_2:
        break

cond_array = [1,2,3,4,5,6,7,8,9]
# 条件３
for rows in matrix_matrix:
    cond_3 = True
    cond_array = [1,2,3,4,5,6,7,8,9]
    for row in rows:
        for cell in row:
            if cell in cond_array:
                cond_array.remove(cell)
            else:
                cond_3 = False
                break
        if not cond_3:
            break
    if not cond_3:
        break

print(YN(cond_1 and cond_2 and cond_3))

