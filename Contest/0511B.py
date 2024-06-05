N, K = map(int, input().split())

A_list = list(map(int, input().split()))

k = K
ans = 0

skipflg = False
while len(A_list) != 0:
    if not skipflg:
        a = A_list.pop()
    
    if k < a:
        # アトラクションスタート
        ans += 1
        k = K
        skipflg = True
    else:
        skipflg = False
        k = k - a
ans += 1
print(ans)
