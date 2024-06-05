import itertools


N = int(input())
N_perm =  sorted(list(itertools.permutations(range(1,N+1))))
p_list = list(map(int, input().split()))

q_list = list(map(int, input().split()))

i = 0
a = 0
b = 0
for n_perm in N_perm:
    i += 1
    if list(n_perm) == p_list:
        a = i
    if list(n_perm) == q_list:
        b = i
print(abs(a - b))