import sys
sys.setrecursionlimit(20000000)
move_list = [(-1, 0),(0, 1),(1, 0),(0, -1)]

H, W = map(int, input().split())
si, sj, gi, gj = map(int, input().split())

input = sys.stdin.readlines
lines = input() 

matrix = []
for line in lines:
    matrix.append(line)                    

visited = []
for h in range(H):
    visited.append([False]*W)

ans = 0
convert_cnt = 2
ans = []
ans_sea = []

def dfs(x, y):
    global convert_cnt
    for move in move_list:
        moved_x = x + move[0]
        moved_y = y + move[1]
        if (moved_x >= H or moved_x < 0  or
            moved_y >= W or moved_y < 0  or
            visited[moved_x][moved_y] == True 
            ):
            continue
        if matrix[moved_x][moved_y] == "." and convert_cnt == 0:
            continue
        elif matrix[moved_x][moved_y] == "." and convert_cnt > 0:
            ans_sea.append((moved_x, moved_y))
            convert_cnt -= 1
        visited[moved_x][moved_y] = True
        if visited[gi-1][gj-1] == True:
            visited[gi-1][gj-1] = False
            ans.append(ans_sea.copy())
            break
        dfs(moved_x, moved_y)
    visited[x][y] = False
    if (convert_cnt == 0 or convert_cnt == 1) and matrix[x][y] == ".":
        convert_cnt += 1
        ans_sea.pop()
    
visited[si-1][sj-1] = True
dfs(si-1, sj-1)

sorted(ans)
dbl_check = []
for a_list in ans:
    if a_list in dbl_check:
        continue
    dbl_check.append(a_list)


print(len(dbl_check))
