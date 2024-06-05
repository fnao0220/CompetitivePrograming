import sys
def alpha():
    return "abcdefghijklmnopqrstuvwxyz"
def alpha_big():
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Aからの相対位置を求める
def alpha_big_num(s):
    return ord(s) - ord("A")
def alpha_num(s):
    return ord(s) - ord("a")
# 1からn迄の連続する整数の合計
def sumk(n):
    return n * (n + 1) // 2 if n >= 1 else 0
# 1からnまでの連続する整数の2乗の合計1^2 + 2^2 + ...
def sumk2(n):
    return n * (n + 1) * (2 * n + 1) // 6 if n >= 1 else 0
def YN(cond):
    return "Yes" if cond else "No"
#  init_tbl(3,4)[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
def init_tbl(H, W, val=0):
    return [[val] * W for i in range(H)]
# 文字列から部分列を求めるmainに含まれるsubを走査
def is_subsequence(sub, main):
    sub_len = len(sub)
    
    if sub_len == 0:
        return True
    
    sub_index = 0
    for char in main:
        if char == sub[sub_index]:
            sub_index += 1
        if sub_index == sub_len:
            return True
            
    return False
