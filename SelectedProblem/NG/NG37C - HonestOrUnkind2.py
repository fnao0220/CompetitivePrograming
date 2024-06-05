from math import dist
import itertools

N = int(input())

cord_list = []

for i in range(N):
    x, y = map(int, input().split())
    cord_list.append((x, y))

perm_list = list(itertools.permutations(cord_list))
dist_sum = 0
for cord_list in perm_list:
    for i in range(1, N):
        dist_sum += dist(cord_list[i - 1], cord_list[i])

print(dist_sum / len(perm_list))
