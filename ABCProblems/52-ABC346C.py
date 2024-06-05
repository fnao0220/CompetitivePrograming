import bisect
N, K = map(int, input().split())

A_list = list(map(int, input().split()))

max_a = max(A_list)

K_list = [ i for i in range(1,K + 1)]

ans = 0

print(sum(K_list))
    