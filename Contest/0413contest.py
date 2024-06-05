#https://qiita.com/drken/items/a803d4fc4a727e02f7ba
N = int(input())

A_list = list(map(int, input().split()))

sum = 0
for Ai in A_list:
    sum += Ai

ans = abs(0-sum)
print(ans)
