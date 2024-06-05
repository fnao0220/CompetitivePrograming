import sys
H, W, N = map(int, input().split())
move_codes = list(input())

input = sys.stdin.readlines
lines = input() 

matrix = []
for line in lines:
    matrix.append(line)


def is_moved(x, y,dbl_check):
    if matrix[x][y] == "#":
        return False
    for move_code in move_codes:
        if move_code == "L":
            move_cord = (0, -1)
        elif move_code == "R":
            move_cord = (0, 1)            
        elif move_code == "U":
            move_cord = (-1, 0)
        elif move_code == "D":
            move_cord = (1, 0)
        moved_x = x + move_cord[0]
        moved_y = y + move_cord[1]
        if (moved_x < 0 or moved_x >= H or
            moved_y < 0 or moved_y >= W or
            matrix[moved_x][moved_y] == "#"
            ):
            return False
        x, y = moved_x, moved_y
    if (x,y) in dbl_check:
        return False
    dbl_check.add((x,y))
    return True

ans = 0
dbl_check = set()
for h in range(H):
    for w in range(W):
        if is_moved(h,w,dbl_check):
            ans += 1
#            print(matrix[h][w])

print(ans)


