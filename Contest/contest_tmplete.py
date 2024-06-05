import sys
def alpha():
    return "abcdefghijklmnopqrstuvwxyz"
def alpha_big():
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Aからの相対位置を求める
def alpha_big_num(s):
    return ord(s) - ord("A")
# 1からn迄の連続する整数の合計
def sumk(n):
    return n * (n + 1) // 2 if n >= 1 else 0
# 1からnまでの連続する整数の2乗の合計1^2 + 2^2 + ...
def sumk2(n):
    return n * (n + 1) * (2 * n + 1) // 6 if n >= 1 else 0
def YN(cond):
    return "Yes" if cond else "No"
