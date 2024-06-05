from itertools import product
N = input()
len = len(N)



ans = 100
for bit in product((0, 1), repeat=len):
    tmp_N = ""
    for k in range(len):
       if bit[k] == 1:
           continue
       tmp_N += N[k]
    if tmp_N == "":
        continue
    if int(tmp_N) % 3 == 0:
        del_keta = sum(bit)
        if ans > sum(bit):
            ans = del_keta

print( -1 if ans == 100 else ans)
          
        
    

