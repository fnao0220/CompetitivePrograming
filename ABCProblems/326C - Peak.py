import bisect

N, M = map(int, input().split())
A_list = list(map(int, input().split()))

A_list = sorted(A_list)

ans = 0 
for n in range(N):
    s_value = A_list[n]
    m = s_value + M
    index_e = bisect.bisect_left(A_list, m)
    if index_e == len(A_list):
        ans = max(ans, N - n)
        break
    ans = max(ans, index_e - n )


print(ans)