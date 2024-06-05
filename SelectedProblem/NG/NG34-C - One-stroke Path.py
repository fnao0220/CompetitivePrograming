N, M = map(int, input().split())

matrix = []
matrix = [[False]*N for _ in range(N)]
visited = [False]*N
for m in range(M):
    a, b = map(int, input().split())
    matrix[a - 1][b - 1] = True
    matrix[b - 1][a - 1] = True

visited_count = 0
visited[0] = True
all_visited = [True]*N
def dfs(i):
    global visited_count
    # 全て訪れた
    if visited == all_visited:
        visited_count += 1
        return
    for n in range(N):
        # 隣接がないor訪問済み
        if matrix[i][n] == False or visited[n] == True:
            continue
        visited[n] = True
        # 隣接地点nから探索開始
        dfs(n)
        # 戻ってきたという事は、隣接地点nからの探索は完了した(=再帰が完了した
        visited[n] = False
        # 地点iからの探索なので、nは未訪問に戻す
    return 

dfs(0)

print(visited_count)

