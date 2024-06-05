N = int(input())

ans_tmp = float("inf")
for n in range(N):
    H, S = map(int, input().split())
    point = H + S * (N-1)
    ans_tmp = min(point, ans_tmp)
    

print(ans_tmp)