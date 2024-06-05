N, M = map(int, input().split())
P_list = []

for n in range(N):
    P_list.append(int(input()))
P_list.sort()

sum_list = []
sum_list.append(0)
sum = 0
for p in P_list:
   sum += p
   sum_list.append(sum)
low = 0
high = sum

print(" ".join(list(map(str,sum_list))))

import bisect
ans = bisect.bisect_left(sum_list, M)

print(ans)
