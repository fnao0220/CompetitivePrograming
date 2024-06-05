N = int(input())
A_list = list(map(int, input().split()))

ans = []
A_list.insert(0,-2) # インデックスと人の値調整
before_to_after_map = {}
for after_man in range(1, N + 1):
    before_man = A_list[after_man]
    if before_man == -1:
        before_to_after_map[-1] = after_man        
    before_to_after_map[before_man] = after_man


man = before_to_after_map[-1]
ans.append(str(man))
while True:
    if man not in before_to_after_map:
        break
    man = before_to_after_map[man]
    ans.append(str(man))
print(" ".join(ans))