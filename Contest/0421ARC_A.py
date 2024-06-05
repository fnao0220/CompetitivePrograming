N, M = map(int, input().split())

matrix = []
for n in range(N):
    matrix.append([0]*N)


#for m in range(M):
#    A, B = map(int, input().split())
#    matrix[A][B] = 1


from itertools import product
#N, M = map(int, input().split())
ans = 0
for pro in product((1, 0), repeat=N):
    print(pro)
    