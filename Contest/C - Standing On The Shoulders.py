N = input()
import sys
input = sys.stdin.readlines
lines = list(input())

sum = 0
all = []
head = -1
for line in lines:
    A, B = line.split()
    A, B = int(A), int(B)
    head = max(head, B - A)
    sum += A

print(sum + head)