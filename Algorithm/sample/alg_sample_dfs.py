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
import sys
R, C = map(int, input().split())
input = sys.stdin.readlines
lines = input() 

matrix = []
for line in lines:
    matrix.append(line)    

s = []
t = []

visited = []
ti, tj = 0, 0
for i in range(R):
    visited.append([False]*C)
    for j in range(C):
        if matrix[i][j] == "s":
            sx, sy = (i, j)      
        if matrix[i][j] == "t":
            ti, tj = (i, j)      
    

move_list = [(-1, 0),(0, 1),(1, 0),(0, -1)]


def dfs(x, y):
    visited[x][y] = True    
    for move in move_list:
        moved_x = x + move[0]
        moved_y = y + move[1]
        
        if (matrix[x][y] == "#" or
            moved_x >= R or moved_x < 0  or
            moved_y >= C or moved_y < 0  
            ):
            continue
        if not visited[moved_x][moved_y]:
            dfs(moved_x, moved_y)

dfs(sx, sy)

        
print ("Yes" if visited[ti][tj] else "No")



