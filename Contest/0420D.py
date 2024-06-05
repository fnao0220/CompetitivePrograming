N, M = map(int, input().split())


A_list = list(map(int, input().split()))

graph = []
for i in range(N):
    row = []
    for j in range(0,N):
        row.append(False)
    graph.append(row)

for m in range(M):
    A, B = map(int, input().split())
    graph[A][B] = True
    graph[B][A] = True
