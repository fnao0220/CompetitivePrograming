# s から t へ辿り着けるか
"""
10 10
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g.#.#.#.#.
#.#.#.#.#.
#.#.#.#.#.
#.....#...
"""
# Cpythonでだそう
import sys
sys.setrecursionlimit(10 ** 7)
H, W = map(int, input().split())
input = sys.stdin.readlines
lines = input() 

matrix = []
for line in lines:
    matrix.append(line)    
s = []
t = []

visited = []
ti, tj = 0, 0
for i in range(H):
    visited.append([False]*W)
    for j in range(C):
        if matrix[i][j] == "s":
            sx, sy = (i, j)      
        if matrix[i][j] == "t":
            ti, tj = (i, j)      
    

move_list = [(-1, 0),(0, 1),(1, 0),(0, -1)]
#             (-1,-1),(1,-1),(1,1),(-1,1)]

def dfs(h, w):
    visited[h][w] = True    
    for move in move_list:
        moved_h = h + move[0]
        moved_w = w + move[1]
        # 縦がh横軸がw
        if (matrix[h][w] == "#" or
            moved_h >= H or moved_h < 0  or
            moved_w >= W or moved_w < 0  
            ):
            continue
        if not visited[moved_h][moved_w]:
            dfs(moved_h, moved_w)

dfs(sx, sy)

        
print ("Yes" if visited[ti][tj] else "No")



