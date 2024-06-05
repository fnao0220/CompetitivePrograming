"""
https://qiita.com/u2dayo/items/8c1601a61841540b4947#%E9%83%A8%E5%88%86%E5%92%8C%E5%95%8F%E9%A1%8C
"""

from itertools import product

N, W = map(int, input().split())
A_List = list(map(int, input().split()))

ans = 0
for pro in product((0,1), repeat = N):
    sum = 0
    for n in range(N):
        if pro[n] == 1:
            sum += A_List[n]
    if sum == W:
        ans += 1
print(ans)