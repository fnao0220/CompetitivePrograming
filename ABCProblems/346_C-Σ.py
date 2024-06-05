#
#
#
# ヒント１：和の公式

N, K = map(int, input().split())
A_list = list(set(map(int, input().split())))

sum_K = K*(K + 1) // 2

sum_A = 0
A_list.sort()
for a in A_list:
    if a > K:
        break
    sum_A += a
    
print(sum_K - sum_A)
