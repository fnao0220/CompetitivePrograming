# https://www.youtube.com/watch?v=Nk2n9fkfSyA
# がわかりやすい
import sys
sys.set_int_max_str_digits(0)
A, B, N = map(int, input().split())


bis
high = 10**9 + 1
low = 0


while abs(high - low) > 1:
    mid = (high + low) // 2
    p = A * int(mid) + B * len(str(mid))

    if p > N:
        high = mid
    else:
        low = mid
print(mid)


