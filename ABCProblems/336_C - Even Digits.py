# 
# 
#インデックス  1 2 3 4 5  6  7  8  9 10
#N　　　　　　 0 2 4 6 8 20 22 24 26 28
# 5個で桁が上がっている⇒5進数
# 5進数　　　　0 1 2 3 4 10 11 12 13 14
# ⇒5進数の2倍になっている

import numpy as np

N = int(input())
print(int(np.base_repr(N - 1, 5))*2)
