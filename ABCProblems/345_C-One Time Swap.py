# 問題文の通りでは成立しない問題
# 考察に至って例を試す
# 例）abca のパターンを書いてみる(入れ替えても変わらないパターンを考慮)
# これの通りは以下になる
# baca △
# cbaa △
# abca　〇元の文字列と同じ
# acba △
# aacb △
# abac △
# 
# 元の文字列と同じとは、同じ文字群から2つを取るので、この場合2C2通り存在する。
# ⇒〇元の文字列と同じ文字列：2C2通り
# 他△は元の文字列とは異なる文字列。これは、全てのパターンは４Ｃ２とわかっているため
# ４Ｃ２ー２Ｃ２で求まる。
import math
from collections import Counter
S = input()

all_comb = math.comb(len(S), 2)

# ペアの数を求める
char_count = Counter(S)

same_count = 0
for str, count in char_count.items():
    if count == 1:
        continue
    same_count += math.comb(count, 2)
diff = all_comb - same_count
ans = diff
if same_count > 0:
    ans += 1

print(ans)

