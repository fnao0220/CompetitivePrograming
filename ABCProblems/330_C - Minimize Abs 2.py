# 全探索
# 10^6ループ
# 2重ループでは間に合わない
# アプローチとして片方を固定
# |x^2 + y^2 - D| ⇒x^2 + y^2が最も近いＤは？
# Dの近さでありうるのは以下の二つ(絶対値なので)
# ±__±__1⃣_D_2⃣__±__±_
#1⃣　x**2 + y ** 2 <= D　で最大を求める
# 4行目よりxは固定されているのでy**2 <= D - x**2で最大のy
# 2⃣はyに＋１すればよい。⇒絶対値なので|x**2 + y**2 -D|でxが固定されているならば,Dより小さくて最大の次は+1でDより大きく最小になる
# 二つ目の解法　y**2 <= D - x**2で最大のy ⇒2文探索の文言



import sys,os
os.chdir(os.path.dirname(__file__))
sys.path.append(os.path.abspath(".."))

import lib.contest_tmplete as contest_tmplete
import math
D = int(input())

ans = float("inf")
for x in range(0,int(math.sqrt(D)) + 1):
    y_side = int(math.sqrt(max(0,D-x**2)))
    
    for y in range(y_side, y_side + 2):
        ans = min(ans, abs(x ** 2 + y ** 2 -D))

print(ans)