N = input()
A_set = set(map(int, input().split()))
M = input()
B_set = set(map(int, input().split()))
L = input()
C_set = set(map(int, input().split()))
Q = input()
X_list = list(map(int, input().split()))

sum_set = set()
for a in A_set:
    for b in B_set:
        for c in C_set:
            sum_set.add(a + b + c)
for x in X_list:
    if x in sum_set:
        print("Yes")
    else:
        print("No")        