# 考察
# 例を試行する
# 例）16
# 16
# 8       8
# 4   4   4   4
# 2 2 2 2 2 2 2 2
#1 1 1 1 1...
# 同じ数字が並んでいる。同じコストを求める必要はない。
import math
from functools import cache
N = int(input())

@cache
def get_cost(x):
    
    if x == 1:
        return 0

    cost = x + get_cost(x // 2)  + get_cost(math.ceil(x / 2))
    return cost
print(get_cost(x))