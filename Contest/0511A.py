N = int(input())
A_list = list(map(int, input().split()))

first_h = A_list[0]
flg = False
for a in range(1,len(A_list)):
    if first_h < A_list[a]:
        flg = True
        break

if flg:
    print(a + 1)
else:
    print(-1)