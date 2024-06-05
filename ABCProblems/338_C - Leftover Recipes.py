N = int(input())

Q_list = list(map(int, input().split()))
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))


max_num = Q_list[0] // A_list[0]
min_q = min(Q_list)

x = 0
max_num = 10 ** 6 + 1
for x in range(max_num):
    y = float("inf")
    for i in range(N):
        zan = (Q[i] - A_list[i]) // B_list[i]  
        y = min(y, zan)
    ans = max(ans, x + y)
print(ans)