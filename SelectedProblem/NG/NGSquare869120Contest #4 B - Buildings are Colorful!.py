from itertools import product
N, K = map(int, input().split())
a_list = list(map(int, input().split()))

ans = 9000000000
for pro in product((0, 1), repeat=N):
    cost = 0
    if sum(pro) != K or pro[0] == 0:
        continue
    maxh = a_list[0]
    for i in range(1,N):
        if pro[i] == 1:
            if i != 0 and maxh >= a_list[i]:
                maxh += 1
                cost += (maxh - a_list[i])
            else:
                cost += 0
        maxh = max(maxh, a_list[i])
    ans = min(ans, cost)  
print(ans)