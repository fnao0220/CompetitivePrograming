from itertools import product
N, M = map(int, input().split())
S = [list(map(int, input().split()))[1:] for _ in range(M)]
P = list(map(int, input().split()))

ans = 0
# スイッチon offのパターン
for bit in product((0, 1), repeat=N):
    on_num = 0
    # 電球でループ
    for m in range(M):
        connect_switchs = S[m]        
        # 電球のスイッチのonの数
        on_sum  = sum(bit[switche - 1] for switche in connect_switchs)
        if on_sum % 2 == P[m]:
            on_num += 1
    if on_num == M:
        ans += 1
print(ans)
 