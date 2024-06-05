N, T = map(str, input().split())
T = list(T)
from sys import stdin
lines = [stdin.readline(10**8)[:-1] for _ in range(int(N))]


def is_subsequence(sub, main):
    sub_len = len(sub)
    main_len = len(main)
    
    if sub_len == 0:
        return True
    
    sub_index = 0
    for char in main:
        if char == sub[sub_index]:
            sub_index += 1
        if sub_index == sub_len:
            return True
            
    return False

ans = []
ans_flg = True
cnt = 0
for S in lines:
#for i in range(int(N)):
#    S = input()
    cnt += 1
    ans_flg = False
    S = list(S)
    
    if len(S) == len(T):
        # 条件１か条件４    
        if S == T:
            ans_flg = True
        else:
            # 条件4
            
            diffcnt = 0
            for s, t in zip(S, T):
                if t != s:
                    diffcnt += 1
                if diffcnt > 1:
                    break
            if diffcnt > 1:
                continue
            ans_flg = True
    elif len(S) == len(T) -1:
        # 条件2
        # 部分列判定
        ans_flg = is_subsequence(S, T)            
    elif len(S) - 1 == len(T):
        # 条件3
        # 部分列判定
        ans_flg = is_subsequence(T, S)            

    if ans_flg:
        ans.append(int(cnt))

ans = sorted(ans)

print(len(ans))
print(" ".join(list(map(str,ans))))