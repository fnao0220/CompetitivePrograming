N = int(input())


A_STRING_list = []
for n in range(N):
    A_STRING_list.append(input())
    
B_STRING_list = []
for n in range(N):
    B_STRING_list.append(input())


for ni in range(N):
    if A_STRING_list[ni] == B_STRING_list[ni]:
        continue
    a = A_STRING_list[ni]
    b = B_STRING_list[ni]
    for nj in range(N):
        a[nj] != b[nj]
        if a[nj] != b[nj]:
            print(str(ni + 1) + " " + str(nj + 1))
            break
        
