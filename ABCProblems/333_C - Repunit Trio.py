N = int(input())

re = []
for r in range(1,20):
    re.append(int("1"*r))

ans_list = []
for r1 in range(len(re)):
    for r2 in range(r1, len(re)):
        for r3 in range(r2, len(re)):
            ans_list.append(re[r1] + re[r2] + re[r3])

ans_list.sort()
#print(len(ans_list))
print(ans_list[N - 1])
