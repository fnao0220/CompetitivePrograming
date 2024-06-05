N, M = map(int, input().split())

import sys
input = sys.stdin.readlines
lines = input()

A_list_list= []
for line in lines:
   A_list_list.append(list(map(int, line.split())))

ans = -1
for m1 in range(M):
    for m2 in range(M):
        point_list = []
        for n in range(N):
            if m1 == m2:
                continue
            point_list.append(max(A_list_list[n][m1], A_list_list[n][m2]))
        ans = max(sum(point_list), ans)

print(ans)
            