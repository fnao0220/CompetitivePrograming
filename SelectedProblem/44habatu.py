from itertools import product
N, K = map(int, input().split())
a_list = list(map(int, input().split()))

ans = float('inf')
for pro in product((0, 1), repeat=N):
    if sum(pro) != K or pro[0] == 0:
        continue
    maxh = a_list[0]
    cost = 0
    for i, b in enumerate(pro):
        if pro[i] == 1:
            if i != 0 and maxh >= a_list[i]:
                maxh += 1
                cost += (maxh - a_list[i])
            else:
                cost += 0
        maxh = max(maxh, a_list[i])
    ans = min(ans, cost)  
print(ans)