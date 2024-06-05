import time

N = int(input())
start = time.time()

ans = len(str(N))
for A in range(1, int(N**0.5) + 1):  # 1からNの平方根までの範囲で探索
    if N % A == 0:
        B = N // A
        ans_tmp = len(str(max(A, B)))
        ans = min(ans_tmp, ans)
print(ans)
end = time.time()
print(end-start,A)

N = int(input())
start = time.time()

max_divisor_digit = len(str(N))  # N自身が最大の約数の場合の桁数

for i in range(1, int(N**0.5) + 1):  # 1からNの平方根までの範囲12で探索
    if N % i == 0:
        divisor_digit = len(str(max(i, N // i)))  # 約数と商の桁数を計算
        max_divisor_digit = min(max_divisor_digit, divisor_digit)
print(max_divisor_digit)

end = time.time()
print(end-start,i)
