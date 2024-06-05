import bisect

N = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
C = sorted(list(map(int, input().split())))

ans = 0
len_c = len(C)
len_a = len(A)
for b in B:
    a_min = bisect.bisect_left(A, b)
    c_min = bisect.bisect_right(C, b)

    ans += a_min * (len_c - (c_min))

print(ans)