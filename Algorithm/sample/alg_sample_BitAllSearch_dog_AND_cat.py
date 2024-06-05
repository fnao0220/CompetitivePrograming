"""
N人に犬派、猫派どちらであるかを聞いた。

犬派なら1、猫派なら2のボタンを押してもらった。

西郷くんはどうやら大の犬好きらしい。そのため、
i(1<=i<=n)番目の人が犬派ならi点貰えるらしい。
合計M点になる場合は何通りあるか？

[入力例]
5 7 (N M)
[出力例]
3
"""
from itertools import product
N, M = map(int, input().split())
ans = 0
for pro in product((1, 2), repeat=N):
    point_sum = 0
    for i in range(len(pro)):
        if pro[i] == 1:
            point_sum += i + 1
    if point_sum == M:
        ans += 1
print(ans)
    