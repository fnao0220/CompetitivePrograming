N = int(input())

A_list = list(map(int, input().split()))

sum = 0
for Ai in A_list:
    sum += Ai

ans = 0-sum
print(ans)
