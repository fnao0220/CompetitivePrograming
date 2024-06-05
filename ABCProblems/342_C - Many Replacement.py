# 最後は最初の文字列で決まる
# 文字aは最終的に何に代わる？
import string
N = int(input())
S = str(input())
Q = int(input())
import sys
input = sys.stdin.readlines
lines = input()

w = string.ascii_lowercase
replace_w_list = []
for line in lines:
    c, d = line.split()
    w = w.replace(c,d)

replace_w_list = list(w)
w_list = string.ascii_lowercase

ans = ""
S = list(S)
for s in S:
    for w, rep_w in zip(w_list, replace_w_list):
        if w == s:
            s = rep_w
            break
    ans += s
            


print("".join(ans))