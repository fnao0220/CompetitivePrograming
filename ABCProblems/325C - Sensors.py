import sys
sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())

input = sys.stdin.readlines
lines = input()

matrix = []
for line in lines:
    matrix.append(line)
    
move_list = [(-1, 0),(0, 1),(1, 0),(0, -1),
             (-1,-1),(1,-1),(1,1),(-1,1)]

visited = []
for i in range(H):
    visited.append([False]*W)

def dfs(x, y):
    if visited[x][y] or matrix[x][y] == ".":
        return False
    visited[x][y] = True    
    for move in move_list:
        moved_x = x + move[0]
        moved_y = y + move[1]
        # 縦がｘ横軸がｙ
        if (moved_x >= H or moved_x < 0  or
            moved_y >= W or moved_y < 0  
            ):
            continue
        if matrix[moved_x][moved_y] == ".":
            continue
        if not visited[moved_x][moved_y]:
            dfs(moved_x, moved_y)
    return True

ans = 0
for h in range(H):
    for w in range(W):
        if dfs(h, w):
            ans += 1


print(ans)

