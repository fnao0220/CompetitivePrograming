from itertools import product

N = int(input())
S = int(input())

ans_value_set = set()
for pro in product((1, 0), repeat=N):
    if sum(pro) == 3:
        ans_value_set.add(pro)
        

