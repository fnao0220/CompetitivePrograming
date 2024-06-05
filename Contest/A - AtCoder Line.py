N, X, Y, Z = list(map(int, input().split()))

station = []

flg = False
if X > Y:
    if Y < Z and Z < X:
        flg = True
if Y > X:
    if X < Z and Z < Y:
        flg = True

if flg:
    print("Yes")
else:
    print("No")
    