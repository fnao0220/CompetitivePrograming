N = int(input())

A_list = list(map(int, input().split()))

min_A = float('inf')
current_man = 0
for a in A_list:
    current_man += a
    min_A = min(min_A, current_man)
    
print(current_man + abs(0 if min_A >= 0 else min_A))