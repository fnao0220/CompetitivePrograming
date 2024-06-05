# 単調像かである事
# ある値を境界として、より下とより上、に分けられる
# 1,   2,   3,   4,    4,   6,   7
# 5を入れると                ↓ここのインデックスが返る
# 1,   2,   3,   4,    4,   6,   7
# 4を入れると    ↓ここのインデックスが返る
# 1,   2,   3,   4,    4,   6,   7
import bisect

N, K  = map(int, input().split())
A = list(map(int, input().split()))

ok = bisect.bisect_left(A, K)

if ok == N:
    print(-1)
else:
    print("ok")
    print(ok)
    print(A[ok])
    
