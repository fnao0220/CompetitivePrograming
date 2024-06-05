N = int(input())

A_list = list(map(int, input().split()))

syo = 10**8
ans = 0
f = 0
for n in range(N - 1):
    # fxc
    f = A_list[n] * (N - n - 1) + sum(A_list[n + 1:])
    f = f % syo
    ans += f


print(ans)
