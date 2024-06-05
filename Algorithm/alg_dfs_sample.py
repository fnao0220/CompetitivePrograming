#https://qiita.com/drken/items/a803d4fc4a727e02f7ba

N, M = map(int, input().split())

import sys
input = sys.stdin.readlines
lines = input()

matrix = []
for line in lines:
    matrix.append(line.strip())
move = [(-1, 0),(0, 1),(1, 0),(0, -1)]

