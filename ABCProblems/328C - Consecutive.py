#m i s s i s s i p p i
#0 0 0 1 1 1 2 2 2 3 3


N, Q = map(int, input().split())
S = list(input())
import sys
input = sys.stdin.readlines
lines = input()

sum = []
sum.append(0)
bef = ""
sum_tmp = 0
for s in S:
    if s == bef:
       sum_tmp += 1
    sum.append(sum_tmp)
    bef = s

for line in lines:
    l, r = map(int, line.split())
    ans = sum[r] - sum[l]
    print(ans)