
N, Q = map(int, input().split())

import sys
input = sys.stdin.readlines
lines = input()

R = (1, 0)
L = (-1, 0)
U = (0, 1)
D = (0, -1)

dragon = []
for n in range(1, N + 1):
    dragon.append((n, 0))

moved_record = []
for line in lines:
    num, cp = line.split()
    if num == "1":
        if cp == "R":
            moved_record.append(R)
        if cp == "L":
            moved_record.append(L)
        if cp == "U":
            moved_record.append(U)
        if cp == "D":
            moved_record.append(D)
    else:
        # 始点に移動
        if len(moved_record) == 0:
            print(" ".join([str(cp),"0"]))
            continue
        calc_moved = moved_record.copy()
        moved_s = (1 - int(cp), 0)
        calc_moved.insert(0, moved_s)
        print(sum(calc_moved))
