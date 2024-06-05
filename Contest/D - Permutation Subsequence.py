N, K = map(int, input().split())
P_list = list(map(int, input().split()))


ans  = float("inf")
for i in range(N):
    for k in range(K):
        for i2 in range( i, N):
            tpl_i = (i, i2)
            tpl_P = (P_list[i], P_list[i2])
            if abs(P_list[i] - P_list[i2]) != 1:
                continue
            print(tpl_i)
            print(tpl_P)
            ans = min(ans, i2 - i)

print(ans)