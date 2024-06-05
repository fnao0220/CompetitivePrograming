S = list(input())
T = list(input())

ans = []
t_start = 0
for s in range(len(S)):
    for t in range(t_start, len(T)):
        if S[s] == T[t]:
            ans.append(t + 1)
            t_start = t + 1
            break
ans = list(map(str, ans))

print(" ".join(ans))