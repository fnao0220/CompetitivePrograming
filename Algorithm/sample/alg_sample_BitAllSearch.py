from itertools import product

n = 3

for pro in product((0, 1), repeat=n):
    print(pro)