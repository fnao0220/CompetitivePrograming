N, Q = map(int, input().split())
T_list = list(map(int, input().split()))

tooth = {}
for n in range(1, N + 1):
    tooth[n] = True


for t in T_list:
    if tooth[t]:
        tooth[t] = False
    else:
        tooth[t] = True
ans = 0
for t,flg in tooth.items():
    if flg:
        ans += 1
        
print(ans)