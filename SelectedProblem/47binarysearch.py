import bisect

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

len_a = len(A)
len_b = len(B)
ans = 0
for a in A:
    index = bisect.bisect_left(B, a)
    if index == len_b:
        break
    for b_index in range(index, len(B)):
        c_index = bisect.bisect_left(C, B[b_index])
#        print(a , B[b_index], C[c_index])
        if c_index == len_b:
           continue
        
        ans += len(C[c_index:])
#        print(a , B[b_index], C[c_index])

print(ans)