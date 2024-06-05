import sys

sys.setrecursionlimit(20000000)
move_list = [(-1, 0),(0, 1),(1, 0),(0, -1),
             (-1, -1),(1, 1),(1, -1),(-1, 1)]


def dfs(x, y):
    for move in move_list:
        moved_x = x + move[0]
        moved_y = y + move[1]
        if (moved_x >= H or moved_x < 0  or
            moved_y >= W or moved_y < 0  or
            visited[moved_x][moved_y] == True 
            ):
            continue
        visited[moved_x][moved_y] = True
        if matrix[moved_x][moved_y] == 0:
            continue
        dfs(moved_x, moved_y)
    

while True:
    W, H = map(int, input().split())
    if (W, H) == (0,0):
        break    
    matrix = []
    visited = []
    for h in range(H):
        matrix.append(list(map(int, input().split())))
        visited.append([False]*W)
    ans = 0
    for h in range(H):
        for w in range(W):
            if matrix[h][w] == 1 and visited[h][w] == False:
                dfs(h,w)
                ans += 1         
    print(ans)


