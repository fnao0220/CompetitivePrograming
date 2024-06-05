N, M = map(int, input().split())
S = list(input())

muziT = M
logoT = 0
ans = 0

for s in S:
    s = int(s)
    if s == 0:
        # 予定無し。シャツ選択
        muziT = M
        logoT = 0
    if s == 1:
        # 無地orロゴ
        if muziT > 0:
            muziT -= 1
        else:
            logoT -= 1
    if s == 2:
        # ロゴのみ
        logoT -= 1
    ans = min(ans, logoT)

print(abs(ans))